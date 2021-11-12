import pymongo
 
 
client = pymongo.MongoClient("mongodb+srv://disneyTracker:disneyTracker@cluster0.0gdpf.mongodb.net/test")
 
# Database Name
db = client["disneyTrackerDb"]
 
# Collection Name
col = db["TrackingApp_user"]
 
x = col.find({})

 
for data in x:
    print(data['userName'],data['userPhone'])

#y = col.find({},{'_id': 0, 'userPhone': 1})


#for data in y:
 #   print(data['userPhone'])

