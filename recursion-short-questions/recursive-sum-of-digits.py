#WAP to find the sum of the digits of a given number using recursion

summ = 0
def digitSum(n):
    if(n == 0):
        return n
    else:
        return (n%10+ digitSum(int(n/10)))
    
num = int(input("Enter the number: "))
print(digitSum(num))
