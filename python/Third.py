# 3. Write a python program to solve quadratic equation
import math

a = 1
b = 5
c = 6

d = b*b - 4*a*c

x1 = (-b + math.sqrt(d)) / (2*a)
x2 = (-b - math.sqrt(d)) / (2*a)

print("Root 1 =", x1)
print("Root 2 =", x2)