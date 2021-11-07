# import MouseTools

# def main(argv):

#     parks = {}
#     wdw = MouseTools.Destination(80007798)
    
#     ids = wdw.get_attraction_ids()
#     for i in range(len(ids)):
#         id = ids[i]
#         a = MouseTools.Attraction(id)

#         print("[%03d / %03d] %s" % (i + 1, len(ids), a.get_name()))
    
#         parkId = a.get_ancestor_park_id()

#         if parkId not in parks:
#             parks[parkId] = []

#         parks[parkId].append(a)

#     for parkId in parks:
#         attractions = None

#         try:
#             park = MouseTools.Park(parkId)
#             attractions = parks[parkId]
#         except:
#             attractions = None

#         if attractions is not None:
#             print(park.get_name() + ": ")
       
#             for a in attractions:
#                 try:
#                     time = a.get_wait_time()
#                     if time is not None:
#                         print("%s - %s" % (str(time), a.get_name()))
#                 except:
#                     pass

#     print(parks,'parks')
#     print(wdw,'wdw')

#     return 0