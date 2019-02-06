# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
""" 

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    
    def testSet1(self): 
        self.assertEqual( classifyTriangle(10, 10, 10), 'Equilateral', '10, 10, 10 should be equilateral' )
    
    def testSet2(self): 
        self.assertEqual( classifyTriangle(3, 4, 5), 'Right', '3, 4, 5 is a Right triangle' )
        self.assertEqual( classifyTriangle(5, 3, 4), 'Right', '5, 3, 4 is a Right triangle' )
        self.assertEqual( classifyTriangle(4, 5, 3), 'Right', '4, 5, 3 is a Right triangle' )
        self.assertEqual( classifyTriangle(5, 12, 13), 'Right', '5, 12, 13 is a Right triangle' )
        self.assertEqual( classifyTriangle(24, 7, 25), 'Right', '24, 7, 25 is a Right triangle' )
    
    def testSet3(self): 
        self.assertEqual( classifyTriangle(4, 5, 6), 'Scalene', '4, 5, 6 should be scalene' )
        self.assertEqual( classifyTriangle(5, 6, 4), 'Scalene', '5, 6, 4 should be scalene' )
        self.assertEqual( classifyTriangle(6, 4, 5), 'Scalene', '6, 4, 5 should be scalene' )

    def testSet4(self):
        self.assertEqual( classifyTriangle(3, 4, 4), 'Isosceles' , '3, 4, 4 should be isosceles' )
        self.assertEqual( classifyTriangle(4, 4, 3), 'Isosceles' , '4, 4, 3 should be isosceles' )
    
    def testSet5(self):
        self.assertEqual( classifyTriangle(2, 3, 10), 'InvalidInput' , '2, 3, 10 is not a triangle' )
        self.assertEqual( classifyTriangle(2, 10, 3), 'InvalidInput' , '2, 10, 3 is not a triangle' )
        self.assertEqual( classifyTriangle(10, 2, 3), 'InvalidInput' , '10, 2, 3 is not a triangle' )
    
    def testSet6(self):
        
        self.assertEqual( classifyTriangle(1, 0.25, 3), 'InvalidInput' , '1, 0.25, 3 is invalid input' )
        self.assertEqual( classifyTriangle(0.25, 1, 3), 'InvalidInput' , '0.25, 1, 3 is invalid input' )
        self.assertEqual( classifyTriangle(1, 3, 0.25), 'InvalidInput' , '1, 3, 0.25 is invalid input' )
        self.assertEqual( classifyTriangle(-1, 4, 4), 'InvalidInput'  , '-1, 4, 4 is invalid input' )
        self.assertEqual( classifyTriangle(4, -1, 4), 'InvalidInput' , '4, -1, 4 is invalid input' )
        self.assertEqual( classifyTriangle(4, 4, -1), 'InvalidInput' , '4, 4, -1 is invalid input' )
        self.assertEqual( classifyTriangle(False, 2, 1), 'InvalidInput' , 'False, 2, 1 is invalid input' )
        self.assertEqual( classifyTriangle(4, False, 1), 'InvalidInput' , '4, False, 1 is invalid input' )
        self.assertEqual( classifyTriangle(4, 2, True), 'InvalidInput' , '4, 2, True is invalid input' )
        
    def testSet7(self):

        self.assertNotEqual( classifyTriangle(3, 4, 4), 'Right', '3, 4, 5 is not a Right triangle' )
        self.assertNotEqual( classifyTriangle(3, 5, 4), 'Equilateral', '3, 5, 4 is not a Equilateral triangle' )
        self.assertNotEqual( classifyTriangle(1, 1, 1), 'Scalene', '3, 5, 4 is not a Equilateral triangle' )
        self.assertNotEqual( classifyTriangle(2, 5, 4), 'Isosceles', '3, 5, 4 is not a Equilateral triangle' )

if __name__ == '__main__':
    print('Running unit tests') 
    unittest.main()

