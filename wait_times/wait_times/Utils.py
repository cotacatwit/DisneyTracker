import os
import sys
import datetime
from filelock import FileLock

def abbrev(s, n):
    if len(s) <= n:
        return s
    else:
        return s[0:n].rstrip() + '...'

def calcStats(stats):
    avg = None
    med = None
    std = None
    n = len(stats)
    if n > 0:
        stats.sort()
        
        if n % 2 == 0:
            median1 = stats[n//2]
            median2 = stats[n//2 - 1]
            med = (median1 + median2) / 2
        else:
            med = stats[n//2]

        avg = int(round(sum(stats) / (n * 1.0)))
        med = int(round(med))

    return (avg, med, std)


def getHistory():
    f = open("/root/wait_times/config/history.cfg", "r")
    history = eval(f.read())
    f.close()
    return history

def setHistory(history):
    f = open("/root/wait_times/config/history.cfg", "w")
    f.write(repr(history))
    f.close()

def getTelephones():
    f = open("/root/wait_times/config/telephones.cfg", "r")
    telephones = eval(f.read())
    f.close()
    return telephones

def setTelephones(telephones):
    f = open("/root/wait_times/config/telephones.cfg", "w")
    f.write(repr(telephones))
    f.close()

def getRules():
    f = open("/root/wait_times/config/rules.cfg", "r")
    rules = eval(f.read())
    f.close()
    return rules

def getAttractions():
    f = open("/root/wait_times/config/attractions.cfg", "r")
    attractions = eval(f.read())
    f.close()
    return attractions

def setRules(rules):
    f = open("/root/wait_times/config/rules.cfg", "w")
    f.write(repr(rules))
    f.close()

def setRule(rule):
    deleteRule(rule)
    rules = getRules()
    rules.append(rule)
    setRules(rules)

def deleteRule(rule):
    rules = getRules()
    newRules = list(filter(lambda x: x["id"] != rule["id"], rules))
    setRules(newRules)

def printRule(rule):
    attractions = getAttractions()
    attractionName = "Unknown"
    if rule["id"] in attractions:
        attractionName = attractions[rule["id"]]
    print(attractionName)

def getLock():
    return FileLock("/root/wait_times/wait_times.lock")
