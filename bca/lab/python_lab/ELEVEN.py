# 11. Write a python Program to Find LCM & GCD using functions
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

x = 12
y = 18

print("GCD =", gcd(x, y))
print("LCM =", lcm(x, y))