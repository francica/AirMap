'''
Created on Feb 26, 2016

@author: francica
'''
import json

class Metro(object):
    def __init__(self, code, name, country, continent, timezone, coordinates, population, region):
        self.code = code
        self.name = name
        self.country = country
        self.continent = continent
        self.timezone = timezone
        self.coordinates = coordinates
        self.population = population
        self.region = region
        

filemap = open("map_data.json").read()
data = json.loads(filemap)
metros = []
for metro in data['metros']:
    m = Metro(metro['code'], metro['name'], metro['country'], metro['continent'], \
              metro['timezone'], metro['coordinates'], metro['population'], metro['region'])
    metros.append(m)
    
print metros[0].code
print metros[0].coordinates
    

