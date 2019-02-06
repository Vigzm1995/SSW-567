import unittest

def classifyTriangle(a,b,c):
    
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return 'InvalidInput'

    #Setting the range of the input values to a maximum of 200.
    if a > 200 or b > 200 or c > 200:return 'InvalidInput'

    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) or not isinstance(b,int) or not isinstance(c,int)):
        return 'InvalidInput'
              
    #Condition of validate that sum of two sides of a triangle is less than the third.
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotAtriangle'
                
    #Conditions for different sides of the triangle
    if a == b and b == a and c == b:
        return 'Equilateral'
    elif ((a ** 2) + (b ** 2)) == (c ** 2):
        return 'Right'
    elif ((b ** 2) + (c ** 2)) == (a ** 2):
        return 'Right'
    elif ((c ** 2) + (a ** 2)) == (b ** 2):
        return 'Right'
    elif (a != b) and  (b != c) and (a != b):
        return 'Scalene'
    else:
        return 'Isosceles'
    
