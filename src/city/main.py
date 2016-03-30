#!/usr/bin/python
#-*-coding:utf-8 -*-
from numpy import empty
from nltk.classify.megam import numpy


'''
Created on Feb 25, 2016

@author: francica
'''

import webbrowser

import json

from metro import Metros
from route import Routes



metros = []
routes = []

def setup():    
    filemap = open("map_data.json").read()
    data = json.loads(filemap)
    for metro_info in data["metros"]:
            metros.append(Metros(**metro_info))
    for route_info in data["routes"]:
            routes.append(Routes(**route_info))


class MetroIsAccess():
    def __init__ (self, name, num):
        self.name = name
        self.num = num
    
    
def getHub(metros, routes): 
    print "*  Here is the CSAir hub cities : "   
    MetroNum = []
    flag = False
    for a in routes:
        flag = False
        for i in range(0, len(MetroNum)):
            if (len(MetroNum)!= 0 and a.ports[0] == MetroNum[i].name) :
                #print "we already have " + MetroNum[i].name + str(i)
                MetroNum[i].num = MetroNum[i].num+1
                flag = True
                
        if(flag == False) : 
            MetroNum.append( (MetroIsAccess(a.ports[0], 1)) )  
     
            #print "now we append" + a.ports[0]    
    for a in routes:
        flag = False
        for i in range(0, len(MetroNum)):
            if (len(MetroNum)!= 0 and a.ports[1] == MetroNum[i].name) :
                #print "we already have " + MetroNum[i].name + str(i)
                MetroNum[i].num = MetroNum[i].num+1
                flag = True
                
        if(flag == False) : 
            MetroNum.append( (MetroIsAccess(a.ports[0], 1)) )  
                     
    max3 = 0
    result = []
    for a in MetroNum:
        if a.num > max3:
            max3 = a.num
            
    for a in MetroNum:
        if a.num == max3:
            result.append(a.name)
    
    return result
    

def getAllCities():
    for metro in metros:
        print metro.name


def getOneCity(self):
    existCity = False
    for metro in (metros):
        if (metro.name == self):
            theMetro = metro
            existCity = True
            print metro
    if existCity:
        print "Here is a list of all other cities that are accessible via a single non-stop flight:\n"
        
        for route in routes:
            if theMetro.code in route.ports[1]:
                print (route.ports[0] + " Distance: " + str(route.distance))
    else:
        print "NO such city in the list"
        
        
def statInfo():
    max1 = 0;
    for a in routes:
       max1 = max(a.distance, max1)   
    print("\n*  The longest single flight in the network is " + str(max1) +" km.\n" )    
    
    min1 = 100000000000;
    for a in routes:
       min1 = min(a.distance, min1)   
    print("*  The shortest single flight in the network is " + str(min1) +" km.\n" )    
    

    l = []
    for a in routes:
       l.append(a.distance)
    average1 = sum(l) / float(len(l)) 
    print("*  The average distance of all the flights in the network is " + str(average1) +" km.\n" )    
    
    
    max2 = 0
    for a in metros:
       if a.population > max2:
           max2 =a.population
           theCity = a.name
    print("*  The biggest city (by population) served by CSAir is " + theCity +".\n" )   
    
    min2 = 10000000000
    for a in metros:
       if a.population < min2:
           min2 =a.population
           theCity2 = a.name
    print("*  The biggest city (by population) served by CSAir is " + theCity2 +".\n" )   
    
    pop = []
    for a in metros:
       pop.append(a.population)
    average2 = sum(pop) / float(len(pop)) 
    print("*  The average population of all the cities served by CSAir is " + str(average2) +".\n" )   
    
    print  "*  List of the continents served by CSAir and which cities are in them: \n" 
    con = []
    for a in metros:
        if a.continent == "South America" :
            con.append(a.name)
    print "    1. Continent : South America contains " + str(con) 
    con = []
    for a in metros:
        if a.continent == "North America" :
            con.append(a.name)
    print "    2. Continent : North America contains " + str(con) 
    con = []
    for a in metros:
        if a.continent == "Asia" :
            con.append(a.name)
    print "    3. Continent : Asia contains " + str(con) 
    con = []
    for a in metros:
        if a.continent == "Africa" :
            con.append(a.name)
    print "    4. Continent : Africa contains " + str(con) 
    con = []
    for a in metros:
        if a.continent == "Europe" :
            con.append(a.name)
    print "    5. Continent : Europe contains " + str(con) 
    getHub(metros, routes)
    
def findAllRoutesConnected(MetroName):
    resRoutes = []
    for a in routes:
        if a.ports[0] == (MetroName) or a.ports[1] == (MetroName) :
            resRoutes.append(a)
                
    return resRoutes

def existElement(metrosList, theOtherMetro):
    for a in metrosList:
        if a == (theOtherMetro):
            return True
        
    return False
    

    
def getShortestDistance(metro1, metro2):
    metroHashTable = {} #declare a hashmap
    metrosList = []
    metrosList.append(metro1)
    i = 0
    while len(metrosList) > i:
        thisMetroName = metrosList[i]
        currentValue = 0
        if metroHashTable.has_key(thisMetroName):
            currentValue = metroHashTable[thisMetroName]
        else: #this is the origin city
            currentValue = 0
            metroHashTable[thisMetroName] = 0
            
        routesConnectedToThisMetro = findAllRoutesConnected(thisMetroName);
        
        for route in routesConnectedToThisMetro:
            theOtherMetro = ""
            distance = route.distance
            if(route.ports[0] == thisMetroName):
                theOtherMetro = route.ports[1]
            else:
                theOtherMetro = route.ports[0]
                
            visited = False
            for j in range(0, i):
                if metrosList[j] == theOtherMetro:
                    visited =True
                    break
            if visited:
                continue
            if metroHashTable.has_key(theOtherMetro):
                metroHashTable[theOtherMetro] = min(metroHashTable[theOtherMetro], distance + currentValue)
            else:
                metroHashTable[theOtherMetro] = distance + currentValue
                
            if existElement(metrosList, theOtherMetro) == False:
                metrosList.append(theOtherMetro)
                
        i = i + 1
        
    finalDistance = 0
    if(metroHashTable.has_key(metro2)):
        finalDistance = metroHashTable[metro2]
        return finalDistance
    else:
        print("The two cities are not connected")
        return -1
   
def deleteCity(city, r):
    i = 0
    cityExist = False
    cityCode = ""
    for a in metros:
        if a.name == city:
            cityCode = a.code
            cityExist = True
            break
        i = i+1
    if cityExist:
        del metros[i]
        print "successfully deleted the city " + city
    else:
        print "There's no city in the CSAir that named " + city
        return r
    #consider the routes being affected 
    routeNew = []
    for a in r:
        if cityCode != a.ports[0] and cityCode != a.ports[1]:
            routeNew.append(a)
        
    return routeNew

def deleteRoute( code1, code2):
    global routes
    i = 0
    routeExist = False
    for a in routes:
        if a.ports[0] == code1 and a.ports[1]==code2:
            routeExist = True
            break
        i = i+1
    if routeExist:
        del routes[i]
        print "Successfully delete the route!"
    else:
        print "No such route in the CSAir!"
            
def putChampaignInData():
                filemap1 = open("cmi_hub.json").read()
                data1 = json.loads(filemap1)
                for metro_info in data1["metros"]:
                    metros.append(Metros(**metro_info))
                for route_info in data1["routes"]:
                    routes.append(Routes(**route_info))
                #now in our database champaign has already been added
                output = dict()
                output["metros"] = []
                output["routes"] = []
                for curr_city in metros:
                    city = dict()
                    city["code"] = curr_city.code
                    city["name"] = curr_city.name
                    city["country"] = curr_city.country
                    city["continent"] = curr_city.continent
                    city["timezone"] = curr_city.timezone
                    city["coordinates"] = curr_city.coordinates
                    city["population"] = curr_city.population
                    city["region"] = curr_city.region
                    output["metros"].append(city)
                for curr_route in routes:
                    r = dict()
                    r["ports"] = curr_route.ports
                    r["distance"] = curr_route.distance
                    output["routes"].append(r)
                with open("combine.json", 'w') as outfile:
                    json.dump(output, outfile, sort_keys=False, indent=4, separators=(',', ':'))
                print("Export combine.json finished!")       
         
def exportNewData():
                output = dict()
                output["metros"] = []
                output["routes"] = []
                for curr_city in metros:
                    city = dict()
                    city["code"] = curr_city.code
                    city["name"] = curr_city.name
                    city["country"] = curr_city.country
                    city["continent"] = curr_city.continent
                    city["timezone"] = curr_city.timezone
                    city["coordinates"] = curr_city.coordinates
                    city["population"] = curr_city.population
                    city["region"] = curr_city.region
                    output["metros"].append(city)
                for curr_route in routes:
                    r = dict()
                    r["ports"] = curr_route.ports
                    r["distance"] = curr_route.distance
                    output["routes"].append(r)
                with open("new_combine.json", 'w') as outfile:
                    json.dump(output, outfile, sort_keys=False, indent=4, separators=(',', ':'))
                print("Export new_combine.json finished!")       
        
def calcRoute(stops):
    numStop = len(stops)
    totalDistance = 0
    
    for i in range(numStop-1):
        existRoute = False
        for a in routes:
            if (stops[i] == a.ports[0] and stops[i+1] == a.ports[1] )\
            or (stops[i] == a.ports[1] and stops[i+1] == a.ports[0]):
                totalDistance = totalDistance + a.distance
                existRoute = True
                break
        if existRoute == False:
            return -1
    if existRoute:
        return totalDistance
    else:
        return -1
                    
def calcCost(stops):   
    numStop = len(stops)
    totalCost = 0
    existRoute = False
    for i in range(numStop-1):
        for a in routes:
            if (stops[i] == a.ports[0] and stops[i+1] == a.ports[1] ) or (stops[i] == a.ports[1] and stops[i+1] == a.ports[0]):                
                if 0.35 - 0.05*i > 0:
                    totalCost = totalCost + a.distance * (0.35 - 0.05*i)
                else:
                    totalCost = totalCost + a.distance * (0)
                
                if (i == numStop-2):
                    existRoute = True
                break
    if existRoute:
        return totalCost
    else:
        return -1  
  
def calcTime(stops):    
    numStop = len(stops)
    layoverTime = 0
    totalTime = 0
    existRoute = False
    for i in range(numStop-1):
        for a in routes:
            if (stops[i] == a.ports[0] and stops[i+1] == a.ports[1] )\
            or (stops[i] == a.ports[1] and stops[i+1] == a.ports[0]):
                layoverTime = layoverTime + (120 - 10 * i )
                dist = a.distance
                if dist <= 400:
                    totalTime += (dist / 750 * 2) * 60  # we use minutes instead of hours
                else:
                    t1 = 200 * 2 / 750 * 60 * 2
                    t2 = (dist - 400) / 750 * 60
                    totalTime += t1 + t2
                
                if (i == numStop-2):
                    existRoute = True
                break
    if existRoute:
        return totalTime + layoverTime
    else:
        return -1  
    
    
#===============================Interface==================================
def everything ():
    global routes
    setup()
            
    while True:
        print "===================================================================\n\n"
        print "* Input 1 for all cities\n"
        print "* Input 2 for detail information of one of the cities\n"
        print "* Input 3 for all statistical information about CSAir\n"
        print "* Input 4 to visualize CSAir's route map\n"
        print "* Input 5 to edit CSAir \n"
        print "* Input 6 to get a new json file for CSAir \n"
        print "* Input 7 to get advanced information about a route \n"
        print "* Input 8 to get shortest air route between two cities \n"
        print "\n\n\n\n More Interesting Fact For CSAir :)\n"
        print "    (●'◡'●)ﾉ♥            <(▰˘◡˘▰)>           ｡◕‿◕｡ \n "
        print "    (*´∇｀*)              (*ﾟ▽ﾟ*)            (｡･ω･)ﾉﾞ   \n "
        print " Σ( ° △ °|||)︴　       ∑(っ °Д °;)っ         (・(ｪ)・)    \n"
        print "====================================================================\n\n"
        
        readIn = input("Please enter your option ")
        
        
        if readIn == 1:
            print "List of all cities:\n"
            getAllCities()
        elif (readIn == 2):
            readIn2 = raw_input("Which city do you want to know? \n")
            getOneCity(readIn2)
        elif (readIn == 3):
            statInfo()
        elif (readIn == 4):
    
            address = "http://www.gcmap.com/mapui?P="
            for a in routes:
                address = address+a.ports[0]+"-"+a.ports[1]+","
            address = address[:-1]
            webbrowser.open(address)
            #userInput2 = input("Input anything to return to menu\n")
            print("================Check your browser!=======================")
        elif (readIn == 5):
            print "* Input 1 to remove city\n"
            print "* Input 2 to remove a route\n" 
            print "* Input 3 to add a city, including all its necessary information\n"
            print "* Input 4 to add a route, including all its necessary information\n"
            print "* Input 5 to edit an existing city\n"
            readIn3 = input(" Please enter your option\n")
            if(readIn3 == 1):
                readIn5 = raw_input(" Please enter the city you want to delete (example: Lima )\n")
                routes = deleteCity(readIn5, routes)
            elif(readIn3 == 2):
                readIn5 = raw_input(" Please enter the route you want to delete (example: LIM-MEX )\n")
                stops = readIn5.split("-")
                routes = deleteRoute(stops[0], stops[1])
            elif(readIn3 == 3):
                myMap = {"code": 1,"name": "default", "country":"default","continent":"default", "timezone":1, "coordinates": '{"N" : 39, "W" : 77}', "population": 1, "region":1}
                newcity = Metros(**myMap)
                newcity.name = raw_input(" Please add city's name: (example: Shenzhen )\n")
                newcity.code = raw_input(" Please add city's code: (example: SZX )\n")
                newcity.country = raw_input(" Please add city's country: (example: CH )\n")
                newcity.continent = raw_input(" Please add city's continent: (example: Asia )\n")
                newcity.timezone = raw_input(" Please add city's timezone: (example: 8 )\n")
                newcity.coordinates = raw_input(" Please add city's coordinates: (example: {'N' : 39, 'W' : 77})\n")
                newcity.population = raw_input(" Please add city's population: (example: 1000000000 )\n")
                newcity.region = raw_input(" Please add city's region: (example: 4 )\n")
                metros.append(newcity)
            elif(readIn3 == 4):    
                routemap = { "ports" : ["MOW" , "IST"] , "distance" : 1763 } 
                newroute = Routes(**routemap)
                newroute.ports[0] = raw_input(" Please add route's origin city's code: (example: CHI )\n")
                newroute.ports[1] = raw_input(" Please add route's origin city's code: (example: IST )\n")
                newroute.distance = raw_input(" Please add route's distance: (example: 11122) )\n")
                routes.append(newroute)
            elif(readIn3 == 5):
                thecity = raw_input("Which city do you want to edit?")
                iscity = False
                for a in metros:
                    if a.name == thecity:
                        iscity = True
                        break
                if iscity:
                    print a
                    a.name = raw_input("New name? Enter the original string if you do not want to change!")
                    a.code = raw_input(" Please change city's code: (example: SZX ). Enter the original string if you do not want to change!\n")
                    a.country = raw_input(" Please change city's country: (example: CH ). Enter the original string if you do not want to change!\n")
                    a.continent = raw_input(" Please change city's continent: (example: Asia ). Enter the original string if you do not want to change!\n")
                    a.timezone = raw_input(" Please change city's timezone: (example: 8 ). Enter the original string if you do not want to change!\n")
                    a.coordinates = raw_input(" Please change city's coordinates: (example: {'N' : 39, 'W' : 77}). Enter the original string if you do not want to change!\n")
                    a.population = raw_input(" Please change city's population: (example: 1000000000 ). Enter the original string if you do not want to change!\n")
                    a.region = raw_input(" Please change city's region: (example: 4 ). Enter the original string if you do not want to change!\n")
                else:
                    print "There is no such city!!!!!!!!!"
                    
        elif (readIn == 6):
            readIn6 = input(" 1 for combine Champaign as a hub city to the old file.\n 2 for generate a currently version json file!\n 3 For test new json can work!")
            if readIn6 == 1:
                putChampaignInData()
            if readIn6 == 2:
                exportNewData()
            if readIn6 == 3:
                filemap = open("new_combine.json").read()
                data = json.loads(filemap)
                new_routes = []
                new_metros = []
                for metro_info in data["metros"]:
                        new_metros.append(Metros(**metro_info))
                for route_info in data["routes"]:
                        new_routes.append(Routes(**route_info))
                        
                for metro in new_metros:
                    print metro.name
                     
        elif (readIn == 7):
            print "Please enter 1 to get the distance of the route you want to know. (example: MEX-CHI-ATL-WAS)\n"
            print "Please enter 2 to get the cost of the route you want to know. (example: MEX-CHI-ATL-WAS)\n"
            print "Please enter 3 to get the time of the route you want to know. (example: MEX-CHI-ATL-WAS)\n"
            readIn8 = input("Enter option:")
            if readIn8 == 1:
                readIn9 = raw_input("Enter route:  (example: MEX-CHI-ATL-WAS)\n")
                stops = readIn9.split("-")
                totalD = calcRoute(stops)
                if totalD == -1:
                    print "NO such route exist"
                else:
                    print "the total route is " + str(totalD) + " km."
            elif readIn8 == 2:
                readIn9 = raw_input("Enter route:  (example: MEX-CHI-ATL-WAS)\n")
                stops = readIn9.split("-")
                thisCost= calcCost(stops)
                if thisCost == -1:
                    print "NO such route exist"
                else:
                    print "the total cost of the route is " + str(thisCost) + "dollars."
                    
            elif readIn8 == 3:
                readIn9 = raw_input("Enter route:  (example: MEX-CHI-ATL-WAS)\n")
                stops = readIn9.split("-")
                TTime = calcTime(stops)
                if TTime == -1:
                    print "NO such route exist"
                else:
                    print "the total time of the route is " + str(TTime) + " minutes."
                    
        elif (readIn == 8):
            readIn4 = raw_input("Which two city do you want to know? (example input: CHI-ATL)\n")
            stops = readIn4.split("-")
            SD = getShortestDistance(stops[0], stops[1])
            print "The shortest distance between " + stops[0] + " and " + stops[1] + " is " +str(SD) + " km."

       
            
if __name__ == "__main__":
    everything()              