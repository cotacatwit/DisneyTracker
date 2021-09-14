import os
import sys
from Utils import *

def main(argv):
   
    attractions = getAttractions()
    attractions.sort(key=lambda x: x["name"])

    for attraction in attractions:
        print("%s %s" % (attraction["id"], attraction["name"]))
    
    return 0

if __name__ == "__main__":
    with getLock():
        main(sys.argv)
