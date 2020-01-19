import sys
sys.path.append("../")
from components import Wall,Mass,Spring,Damper,Forcing
from collections import OrderedDict

def findObj(objects,name):
    if name in objects["walls"]:
        return objects["walls"][name]
    if name in objects["masses"]:
        return objects["masses"][name]
    if name in objects["springs"]:
        return objects["springs"][name]
    if name in objects["dampers"]:
        return objects["dampers"][name]
    if name in objects["forcings"]:
        return objects["forcings"][name]

def validateSetup(s):
    walls=OrderedDict()
    masses=OrderedDict()
    springs=OrderedDict()
    dampers=OrderedDict()
    forcings=OrderedDict()
    #SORT
    for obj in s:
        if type(obj[1])==Wall:
            walls[obj[0]]=obj[1]
        if type(obj[1])==Mass:
            masses[obj[0]]=obj[1]
        if type(obj[1])==Spring:
            springs[obj[0]]=obj[1]
        if type(obj[1])==Damper:
            dampers[obj[0]]=obj[1]
        if type(obj[1])==Forcing:
            forcings[obj[0]]=obj[1]

    #print(springs)

    for springName,springObj in springs.items():
        #print(springObj.linkA,springObj.linkB)
        if springObj.linkA in masses:
            masses[springObj.linkA].springs.append((springObj.linkB,springObj))
        if springObj.linkB in masses:
            masses[springObj.linkB].springs.append((springObj.linkA,springObj))

    for damperName,damperObj in dampers.items():
        #print(springObj.linkA,springObj.linkB)
        if damperObj.linkA in masses:
            masses[damperObj.linkA].dampers.append((damperObj.linkB,damperObj))
        if damperObj.linkB in masses:
            masses[damperObj.linkB].dampers.append((damperObj.linkA,damperObj))

    for forcingName,forcingObj in forcings.items():
        if forcingObj.link in masses:
            masses[forcingObj.link].forcings.append(forcingObj)

    return {"walls":walls,"masses":masses,"springs":springs,"dampers":dampers,"forcings":forcings}
