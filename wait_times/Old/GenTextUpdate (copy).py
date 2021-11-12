import os
import sys
import smtplib
import ssl
import pymongo

def main(argv):

    client = pymongo.MongoClient("mongodb+srv://disneyTracker:disneyTracker@cluster0.0gdpf.mongodb.net/test")

    # Database Name
    db = client["disneyTrackerDb"]

    # Collection Name
    col = db["TrackingApp_suggestThriller"]

    #for r in col.find({}):
        #print(r)

    #Find specific data in collection
    x = col.find({})
    for data in x:

        #return User's name and phone number
        #for data in x:
        #print(data['userName'],data['userPhone'])
        smtp_server = "smtp.gmail.com"
        port = 587
        sender_email = "disneytracker2021@gmail.com"
        password = "Wentworth1234!"

        context = ssl.create_default_context()

      	ride = data['rideName']
      	waitime = data['rideWaitTime']
        message = "Here are some of our suggestions as well!\n\n"
        message += "-" + ride + " wait time is " + waittime + " minutes\n\n"

        print(message)


        try:
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, address, message)


        except Exception as e:
            print(e)

        finally:
            server.quit()

            


if __name__ == "__main__":
    main(sys.argv)

