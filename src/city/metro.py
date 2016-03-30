'''
Created on Feb 25, 2016

@author: francica
'''

import json
    
class Metros(object):
    def __init__(self, **kwargs):
        for keyword in ["code", "name", "country", "continent", "timezone", "coordinates", "population", "region"]:
            setattr(self, keyword, kwargs[keyword])
    
    def __str__(self):
        fields = ['{}: {}'.format(k,v) for k,v in self.__dict__.iteritems()]
        return "{}(\n{})".format("Detail Information", '\n'.join(fields))
    


filemap = open("map_data.json").read()
data = json.loads(filemap)

metros = []
for metro_info in data["metros"]:
        metros.append(Metros(**metro_info))


#myMap ={}
#myMap = {"code": 3,"name": "dasas", "country":"dadas","continent":"daasd", "timezone":1, "coordinates": '{"N" : 39, "W" : 77}', "population": 12321, "region":3}        
#myMap["code"] = 1
#m = Metros(**myMap)
#print m.code
        #dataMetros = json.loads(data["metros"], object_hook = object_decoder)

#for metro in metros:
#    print metro 
    

'''                
        self.code = code
        self.name = name
        self.country = country
        self.continent = continent
        self.timezone = timezone
        self.coordinates = coordinates
        self.population = population
        self.region = region
'''    
        