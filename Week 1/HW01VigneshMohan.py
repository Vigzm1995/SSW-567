'''
    File Name: HW01VigneshMohan (567).py
    Script Author: Vignesh Mohan
    Purpose: Week 1 Assignment.
    Python Version: 3.0
'''

'''Program for testing triangle classification'''

#Importing the unittest, automated test platform library.
import unittest   

#Functions for classifying different types of triangles.
def classify_triangle(a,b,c):
    
    if a == b and b == c:
        print("Equilateral triangle")
        t_type = 'Equilateral'
    elif a==b or b==c:
        print("Isosceles triangle")
        t_type = 'Isosceles'
    else:
        print("Scalene triangle")
        t_type = 'Scalene'

    return t_type

#Function for right angeled triangle.
def right_angle(a, b, c):
    
    if (a * a) + (b * b) == (c * c):
        t_type = 'Right'

    return t_type

def main():

    #User input for different sides of the triangle.
    print("\nInput lengths of the triangle sides: ")

    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

class TestTriangles(unittest.TestCase):

    #Checking the test cases for a right angeled triangle.
    def testSet1(self): 
        self.assertEqual(right_angle(3, 4, 5),'Right')
        #self.assertNotEqual(right_angle(1,1,1.414213),'Right')   

    #Checking the test cases for different types of triangles.
    def testSet2(self): 

        self.assertEqual(classify_triangle(233,233,233),'Equilateral')
        self.assertEqual(classify_triangle(2,3,3),'Isosceles')
        self.assertEqual(classify_triangle(10,15,30),'Scalene')
        self.assertEqual(classify_triangle(10,10,1),'Isosceles')
        self.assertEqual(classify_triangle(1,2,3),'Scalene')
        self.assertEqual(classify_triangle(10,15,30),'Scalene')
        self.assertNotEqual(classify_triangle(19,9,9),'Equilateral')
        self.assertNotEqual(classify_triangle(10,10,10),'Isosceles')

#Invoking the function calls from the main function.
if __name__ == '__main__':

    classify_triangle
    right_angle
    unittest.main(exit=False,verbosity=2)
