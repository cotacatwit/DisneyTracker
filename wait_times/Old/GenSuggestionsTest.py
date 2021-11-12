import pymongo
 

client = pymongo.MongoClient("mongodb+srv://disneyTracker:disneyTracker@cluster0.0gdpf.mongodb.net/test")
 
db = client["disneyTrackerDb"]
 
# Collection Name
col = db["TrackingApp_user"]
col2 = db['TrackingApp_suggestThriller']
col3 = db['TrackingApp_suggestSit']
col4 = db['TrackingApp_suggestShow']
col5 = db['TrackingApp_suggestKids']
col6 = db["TrackingApp_ride"]
 
x = col.find({})
 
for data in x:
    favorite = data['userFavorite']
    print(favorite)
    address = data['userPhone']
    print(address)

    favList = col2.find_one({'rideName':favorite})

    if favList is not None:
        y = col2.find({})
        for data in y:
            rideList = data['rideName']
            print(rideList)
            for ride in rideList:
                    waittime =  col6.find_one({'rideName': rideList})['rideWaitTime']
                 
            print(waittime)

    favList2 = col3.find_one({'rideName':favorite})

    if favList2 is not None:
        y = col3.find({})
        for data in y:
            rideList = data['rideName']
            print(rideList)

    favList3 = col4.find_one({'rideName':favorite})

    if favList3 is not None:
        y = col4.find({})
        for data in y:
            rideList = data['rideName']
            print(rideList)

    favList4 = col5.find_one({'rideName':favorite})

    if favList4 is not None:
        y = col5.find({})
        for data in y:
            rideList = data['rideName']
            print(rideList)






    




