#1
import math

def degree_to_radian(degrees):
    return degrees * (math.pi / 180)

degrees = float(input("Input Degree: "))
radians = degree_to_radian(degrees)
print("Output radian: ", radians)


#2
def trapezoid_area(a, b, h):
    return 0.5 * (a + b) * h

h = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))

area = trapezoid_area(a, b, h)
print("Expected Output:", area)

#3
import math

def regular_polygon_area(n, s):
    perimeter = n * s
    apothem = s / (2 * math.tan(math.pi / n))
    return 0.5 * perimeter * apothem

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

area = regular_polygon_area(n, s)
print("The area of the polygon is: ", area)


#4
def parallelogram_area(base, height):
    return base * height

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = parallelogram_area(base, height)
print("Expected Output:", area)
