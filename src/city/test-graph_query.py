'''
Created on Feb 26, 2016

@author: francica
'''

from unittest import TestCase
import main
#initilized
main.setup()


class testQuery(TestCase):

    def test_hub(self):
        a = main.getHub()
        self.assertEqual(u'LIM', a[1].name)
        self.assertEqual(3, a[1].num)
        self.assertEqual(u'CAI', a[10].name)
        self.assertEqual(4, a[33].num)
        self.assertEqual(4, a[45].num)
        
    
        
        
if __name__ == "__main__":
    unittest.main()
'''

'''
