#WAP to find out if a number is prime using recursion

i = 2
def isPrime(n):
    global i
    if(n==i):
      print("The number is a prime number")  
    elif n%i == 0:
        print("The number is not a prime number")
    else:
        i=i+1
        isPrime(n)

num = int(input("Enter a number: "))
isPrime(num)