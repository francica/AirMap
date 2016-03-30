'''
Created on Feb 25, 2016

@author: francica
'''
import json

class Routes(object):
    def __init__(self, **kwargs):
        for keyword in ["ports", "distance"]:
            setattr(self, keyword, kwargs[keyword])
    
    def __str__(self):
        fields = ['{}: {}'.format(k,v) for k,v in self.__dict__.iteritems()]

        return "{}(\n{})".format(self.__class__.__name__, '\n'.join(fields))

filemap = open("map_data.json").read()
data = json.loads(filemap)

route = []
for route_info in data["routes"]:
        route.append(Routes(**route_info))
        #dataMetros = json.loads(data["metros"], object_hook = object_decoder)


#for r in route:
#    print r.distance
