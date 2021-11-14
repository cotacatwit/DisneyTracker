import os
import sys
import smtplib
import ssl
import pymongo

from datetime import date
from email.message import EmailMessage

def main(argv):

    client = pymongo.MongoClient("mongodb+srv://disneyTracker:disneyTracker@cluster0.0gdpf.mongodb.net/test")

    # Database Name
    db = client["disneyTrackerDb"]

    # Collection Name
    col = db["TrackingApp_user"]
    col6 = db["TrackingApp_ride"]
    col2 = db['TrackingApp_suggestthriller']
    col3 = db['TrackingApp_suggestsit']
    col4 = db['TrackingApp_suggestshow']
    col5 = db['TrackingApp_suggestkids']

    today = str(date.today())

    #for r in col.find({}):
        #print(r)

    #Find specific data in collection
    x = col.find({})
    for data in x:
        datesAll = data['userDates'].split(',')
        userUpdateTime = data['userUpdateTime']
        for date1 in datesAll:
            singleDate = col.find_one({'userDate':date1})
            if date1 == today:
                if userUpdateTime == '5':
                    #return User's name and phone number
                    #for data in x:
                    #print(data['userName'],data['userPhone'])
                    smtp_server = "smtp.gmail.com"
                    port = 587
                    sender_email = "disneytracker2021@gmail.com"
                    password = "Wentworth1234!"

                    context = ssl.create_default_context()

                    rides = data['userRides'].split(',')
                    address = data['userPhone']
                    print(address)
                    message = "Hello "
                    message += data['userName']
                    message += "!"
                    message += "\n\nHere are your current wait time updates:\n\n"
                    #message += data['userRides'].replace(",", "\n- ")

                    for ride in rides:
                        #Finds the wait time of user specific rides
                        waittime =  col6.find_one({'rideName': ride})['rideWaitTime']
                        message += "-" + ride + " wait time is " + waittime + " minutes\n\n"

                    message += "\nHave fun!"

                    print(message)


                    msg = EmailMessage()
                    msg['Subject'] = "Update!"
                    msg.set_content(message)
                    msg['From'] = sender_email
                    msg['To'] = address

                    try:
                        server = smtplib.SMTP(smtp_server, port)
                        server.ehlo()
                        server.starttls(context=context)
                        server.ehlo()
                        server.login(sender_email, password)
                        server.send_message(msg)


                    except Exception as e:
                        print(e)

                    finally:
                        server.quit()



                    favorite = data['userFavorite']
                    print(favorite)
                    address = data['userPhone']
                    print(address)
                    message = "Here are some of our suggestions!\n\n"

                    favList = col2.find_one({'rideName':favorite})

                    if favList is not None:
                        y = col2.find({})
                        for data in y:
                            rideList = data['rideName']
                            print(rideList)
                            for ride in rideList:
                                waittime =  col6.find_one({'rideName': rideList})['rideWaitTime']
                            message += "-" + rideList + " wait time is " + waittime + " minutes\n\n"


                    favList2 = col3.find_one({'rideName':favorite})

                    if favList2 is not None:
                        y = col3.find({})
                        for data in y:
                            rideList = data['rideName']
                            print(rideList)
                            for ride in rideList:
                                waittime =  col6.find_one({'rideName': rideList})['rideWaitTime']
                            message += "-" + rideList + " wait time is " + waittime + " minutes\n\n"



                    favList3 = col4.find_one({'rideName':favorite})

                    if favList3 is not None:
                        y = col4.find({})
                        for data in y:
                            rideList = data['rideName']
                            print(rideList)
                            for ride in rideList:
                                waittime =  col6.find_one({'rideName': rideList})['rideWaitTime']
                            message += "-" + rideList + " wait time is " + waittime + " minutes\n\n"



                    favList4 = col5.find_one({'rideName':favorite})

                    if favList4 is not None:
                        y = col5.find({})
                        for data in y:
                            rideList = data['rideName']
                            print(rideList)
                            for ride in rideList:
                                waittime =  col6.find_one({'rideName': rideList})['rideWaitTime']
                            message += "-" + rideList + " wait time is " + waittime + " minutes\n\n"


                    message += "\nHave fun!"

                    print(message)


                    msg = EmailMessage()
                    msg.set_content(message)
                    msg['Subject'] = "Suggestions!"
                    msg['From'] = sender_email
                    msg['To'] = address

                    try:
                        server = smtplib.SMTP(smtp_server, port)
                        server.ehlo()
                        server.starttls(context=context)
                        server.ehlo()
                        server.login(sender_email, password)
                        server.send_message(msg)



                    except Exception as e:
                        print(e)

                    finally:
                        server.quit()




if __name__ == "__main__":
    main(sys.argv)

