#Herons Formula
import math

#returns the square root of the number n
def root(n):
    return math.sqrt(n)

#Takes in the 3 side lengths of a triangle as arguments and returns half of
#the perimeter of a triangle.
def semiPerimeter(n1,n2,n3):
    semiPerimeter = (n1+n2+n3)/2
    return(semiPerimeter)


#Modify the below function such that it takes in 4 arguments. multiply the first
#argument by the difference between itself and each individual argument. Reference herons formula for more context.
def multiplyDifferences(s, a, b, c):
    # d=semiPerimeter(n1,n2,n3)
    x = s* (s-a) * (s-b) * (s-c)
    return x

#Given the 3 sides of a triangle return the area.
#use herons formula
#Use the functions above.
def herons(a,b,c):
    s = semiPerimeter(a,b,c)
    Area=multiplyDifferences(s, a,b,c)
    Area = root(Area)
    return Area


#quadratic equation

#takes in a number as an argument and returns that number multiplied by 2.
def denominator(a):
    # y = ax**2+bx+c
    # z = 2(ax**2+bx+c)
    return(2*a)

#Takes in two arguments. multiply the first argument by negative 1. Then
#return the modified first argument added and subtracted by the second argument.
def plusMinus(x, y):
    b = -1*x
    return b-y, b+y

#takes in three numbers as arguments. The first and third multiplied together then
#multiplied by 4.Then subtract that result from the second argument squared.
#Return the overall result.
def mainCalc(a, b, c):
    x = (a*c*4)
    y = (b**2)
    z = y-x
    return z


#The below function should take the inputs of the quadratic equation and return the result
#Make sure to use all the formulas from this section.
def quadratic(a, b, c):
    m = mainCalc(a, b, c) #b**2 - 4ac
    s = root(m) #square root
    x1, x2 = plusMinus(b,s) #x1 = -b + the square root of b**2 - 4ac, x2 = -b - the square root of b**2 - 4ac
    d = denominator(a) #2a
    return x1/d, x2/d # x1/d = (-b + the square root of b**2 - 4ac)/2a, x2/d = (-b - the square root of b**2 - 4ac)/2a

# def root(n):
#     return math.sqrt(n)

# def denominator(a):
#     return(2*a)

# def plusMinus(x, y):
#     b = -1*x
#     return b-y, b+y

# def mainCalc(a, b, c):
#     x = (a*c*4)
#     y = (b**2)
#     z = y-x
#     return z