import os
import sys
import string
import MouseTools
import datetime
import smtplib
import ssl
from Utils import *

def main(argv):

    now = datetime.datetime.now()
    
    hour = int("{:%H}".format(now))
    minute = int("{:%I}".format(now))

    # Clear history at 4AM
    if hour == 4:
        setHistory([])

    notifications = []
    messages = []
    notificationsByPark = {}
    rules1 = getRules()
    history = getHistory()

    ##############################################
    ### 1. Get wait times for each attraction
    ##############################################

    for rule in rules1:

        # Get attraction wait time
        try:
            attraction = MouseTools.Attraction(rule["id"])
            waitTime = attraction.get_wait_time()

            print("%s - %s" % (attraction.get_name(), str(waitTime)))

            # If not closed add to notification list
            if waitTime is not None:

                history.append({
                    "attraction": attraction.get_id(),
                    "time": waitTime,
                    "date": now
                })

                if waitTime <= rule["max"]:
                    notifications.append({
                        "id": attraction.get_id(),
                        "attraction": attraction,
                        "name": attraction.get_name(),
                        "time": waitTime
                    })
        except:
            continue

    setRules(rules1)
    setHistory(history)

    # Bail if no notifications need to be sent
    if len(notifications) == 0:
        print("No notifications")
        return 0

    ##############################################
    ### 2. Organize by park
    ##############################################

    for n in notifications:

        attraction = n["attraction"]
        parkId = attraction.get_ancestor_park_id()
        
        # Add park list if not added yet
        if parkId not in notificationsByPark:
            notificationsByPark[parkId] = []
        
        notificationsByPark[parkId].append(n)

    ##############################################
    ### 3. Generate texts
    ##############################################

    message = "Subject: Updates!\n%u Update" % len(notifications)
    if len(notifications) > 1 or len(notifications) == 0:
        message += "s"
    message += " at "
    message += "{:%m/%d/%Y %I:%M %p}".format(now)
    message += ":\n\n"

    for parkId in notificationsByPark:
        park = MouseTools.Park(parkId)
        message += (park.get_name() + ":\n\n")
        notifications = notificationsByPark[parkId]
        
        # Sort by wait time in non-decreasing order
        notifications.sort(key=lambda x: x["time"])

        for n in notifications:

            # get historic wait times for this id
            attractionHistory = list(filter(lambda x: x["attraction"] == n["id"], history))
            attractionHistory = list(map(lambda x: x["time"], attractionHistory))
            historyLen = len(attractionHistory)

            # calc average
            avg = 0
            if historyLen > 0:
                avg = int(round(sum(attractionHistory) / (historyLen * 1.0)))

            message += "- " + abbrev(n["name"], 35) + ": " 
            message += "(%s/%s)" % (str(n["time"]), str(avg))
            message += "\n"
        message += "\n"

    message = message[:-1]
    message = ''.join(filter(lambda x: x in string.printable, message))
    print(message)

    ##############################################
    ### 4. Build destination addresses
    ##############################################

    addresses = []
    telephones = getTelephones()
    
    for telephone in telephones:

        if "lastTime" not in telephone:
            telephone["lastTime"] = None

        if "active" not in telephone:
            telephone["active"] = False

        lastTime = telephone["lastTime"]
        active = telephone["active"]
        send = False
        
        # Check if we can send to this telephone 
        if lastTime is not None:
            diff = (now - lastTime).total_seconds() / 60.0
            if diff > telephone["freq"]:
                send = True
            else:
                print("%s not ready" % (telephone["email"]))
        else:
            send = True

        if not active:
            send = False

        # Add address and update last send time
        if send:
            telephone["lastTime"] = now
            addresses.append(telephone["email"])
   
    setTelephones(telephones)

    if len(addresses) == 0:
        print("No addresses to send to")
        return 0

    ##############################################
    ### 5. Send 
    ##############################################

    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "disneytracker2021@gmail.com"

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, addresses, message)

    except Exception as e:
        print(e)
    finally:
        server.quit()

    return 0

if __name__ == "__main__":
    with getLock():
        main(sys.argv)
