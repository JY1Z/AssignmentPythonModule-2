import math
import random


name = input("Enter your name:")
print("Hello, "+name+"!")


r = float(input("the radius of a circle is:"))
pi = math.pi
area = r * r * pi
print("the area of the circle:", area)


length = float(input(" the length of a rectangle:"))
width = float(input(" the width of a rectangle:"))
perimeter = 2 * length + 2 * width
Area = length * width
print(" the perimeter of the rectangle:", perimeter)
print(" the area of the rectangle:", Area)


A = int(input("enter an integer number:"))
B = int(input("enter an integer number:"))
C = int(input("enter an integer number:"))
Sum = A + B + C
product = A * B * C
average = Sum/3
print("the sum of the numbers:", sum)
print("the product of the numbers:", product)
print("the average of the numbers:", average)


talents = float(input("Enter talents:"))
pounds = float(input("Enter pounds:"))
lots = float(input("Enter lots:"))
t = talents * 20 * 32 * 13.3
p = pounds * 32 * 13.3
L = lots * 13.3
Sum = t + p + L
integer = Sum/1000
integer = int(integer)
residue = Sum - integer * 1000
residue = ("%.2f" % residue)
print("The weight in modern units:")
print(integer, "kilograms and", residue, "grams.")


a1 = str(random.randint(0, 9))
a2 = str(random.randint(0, 9))
a3 = str(random.randint(0, 9))
b1 = str(random.randint(1, 6))
b2 = str(random.randint(1, 6))
b3 = str(random.randint(1, 6))
b4 = str(random.randint(1, 6))
print("Draws two random combinations of numbers for a combination lock:", a1+a2+a3, b1+b2+b3+b4)