'''
Created on Feb 26, 2016

@author: francica
'''

from unittest import TestCase
import main
import json
from metro import Metros
from route import Routes
#initilized
main.setup()


class testParse(TestCase):

    def test_listLength(self):
        self.assertEqual(48, len(main.metros))
        self.assertEqual(94, len(main.routes))
        
    def test_parseMetro(self):
        self.assertEqual("Lima", main.metros[1].name)
        self.assertEqual("Buenos Aires", main.metros[4].name)
        self.assertEqual({u'S': 35, u'W': 58}, main.metros[4].coordinates)
        self.assertEqual("Sao Paulo", main.metros[5].name)
        self.assertEqual("Toronto", main.metros[47].name)
        self.assertEqual("New York", main.metros[46].name)
        self.assertEqual("Washington", main.metros[45].name)

    def test_editRoute(self):
        self.assertEqual(4231, main.routes[1].distance)
        self.assertEqual("CHI", main.routes[4].ports[1])
        self.assertEqual("MEX", main.routes[4].ports[0])
        self.assertEqual([u'MEX', u'MIA'], main.routes[5].ports)
        self.assertEqual([u'BGW', u'RUH'], main.routes[44].ports)
        self.assertEqual(575, main.routes[91].distance)
        self.assertEqual(1483, main.routes[90].distance)
    
    def test_savingJson(self):
        filemap = open("combine.json").read()
        data = json.loads(filemap)
        new_routes = []
        new_metros = []
        for metro_info in data["metros"]:
            new_metros.append(Metros(**metro_info))
        for route_info in data["routes"]:
            new_routes.append(Routes(**route_info))
        self.assertEqual([u'CMI'], main.getHub(new_metros, new_routes))
    
    def test_ShortestPath(self):
            metros = []
            routes = []
            filemap = open("map_data.json").read()
            data = json.loads(filemap)
            for metro_info in data["metros"]:
                metros.append(Metros(**metro_info))
            for route_info in data["routes"]:
                routes.append(Routes(**route_info))
            self.assertEqual(11881, main.getShortestDistance("LAX", "LED"))
            self.assertEqual(10592, main.getShortestDistance("LAX", "ALG"))

        
if __name__ == "__main__":
    unittest.main()