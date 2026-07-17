# 20. Write a python program to demonstrate exception handling
try:
    a = 10
    b = 0
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Cannot divide by zero")