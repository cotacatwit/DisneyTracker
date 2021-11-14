import pymongo
 
 
client = pymongo.MongoClient("mongodb+srv://disneyTracker:disneyTracker@cluster0.0gdpf.mongodb.net/test")

 
# Database Name
db = client["disneyTrackerDb"]
 
# Collection Name
col = db["TrackingApp_user"]
 
x = col.find()
 
for data in x:
    userUpdateTime = data['userUpdateTime']
    print(userUpdateTime)
    datesAll = data['userDates'].split(',')
    for date in datesAll:
        singleDate = col.find_one({'userDate':date})
        print(date)
