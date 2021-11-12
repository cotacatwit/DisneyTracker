import os
import sys
from Utils import *

def main(argv):
   
    rules = getRules()

    for rule in rules:
        printRule(rule)

    setRules([])
    return 0

if __name__ == "__main__":
    ret = 0
    with getLock():
        ret = main(sys.argv)
    exit(ret)
