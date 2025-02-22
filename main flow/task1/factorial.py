def factorial(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res
n=5
print(f"the factorial of {n} is {factorial(n)}.")
