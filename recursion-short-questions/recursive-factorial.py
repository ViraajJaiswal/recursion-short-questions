#WAP to find factorial using recursion

def factorial(n):
    if n == 1:
        return n
    else:
        return n*(factorial(n-1))

a = int(input("Enter a number "))
print(factorial(a))