import math

def gcd(a, b):
    return math.gcd(a, b)
num1 = 48
num2 = 18
print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}.")
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
num1 = 48
num2 = 18
print(f"The LCM of {num1} and {num2} is {lcm(num1, num2)}.")
