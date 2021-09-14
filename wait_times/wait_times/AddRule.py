import os
import sys
import MouseTools
from Utils import *

def main(argv):
   
    #id = int(input("Attraction ID: "))
    #max = int(input("Max Wait Time: "))
    #freq = int(input("Notify Frequency: "))

    ids = [
        80010199, 
        80010224, 
        80010149, 
        80010123, 
        26068, 
        207395, 
        80010153, 
        80010157, 
        80010173, 
        80010176, 
        20194,
        80010190,
        80010191,
        80010192, 
        80010110, 
        16767284, 
        80010208,
        80010161,
        19263736,
        80010177,
        80010114,
        19259335,
        80010218
        ]

    # Get unique
    ids = list(set(ids))
    
    for id in ids:

        a = MouseTools.Attraction(id) 

        if a is not None:
            
            print("%s %s" % (str(id), a.get_name()))

            rule = {
                "id": id,
                "max": 45,
                "freq": 0
            }
    
            setRule(rule)

    return 0

if __name__ == "__main__":
    ret = 0
    with getLock():
        ret = main(sys.argv)
    exit(ret)
