import os
import sys
import MouseTools

def updateParks():
    
    print("Updating parks...")
    wdw = MouseTools.Destination(80007798)
    parks = []
    
    print("Getting park IDs")

    ids = wdw.get_park_ids()

    for i in range(len(ids)):
        id = ids[i]
        p = MouseTools.Park(id)
        
        print("[%03d / %03d] Updating park %s (%s)" % (i + 1, len(ids), p.get_name(), id))

        park = {}
        park["id"] = id
        park["name"] = p.get_name()
        parks.append(park)

    f = open("config/parks.cfg", "w")
    f.write(repr(parks))
    f.close()

def updateAttractions():

    print("Updating attractions...")
    wdw = MouseTools.Destination(80007798)
    attractions = []

    ids = wdw.get_attraction_ids()

    for i in range(len(ids)):
        id = ids[i]
        a = MouseTools.Attraction(id)

        print("[%03d / %03d] Updating attraction %s (%s)" % (i + 1, len(ids), a.get_name(), id))

        attraction = {}
        attraction["id"] = id
        attraction["name"] = a.get_name()
        attractions.append(attraction)

    f = open("config/attractions.cfg", "w")
    f.write(repr(attractions))
    f.close()

def main(argv):
    updateParks()
    updateAttractions()
    return 0

if __name__ == "__main__":
    exit(main(sys.argv))
