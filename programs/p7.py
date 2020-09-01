#Write a Pyhton program to claculate GCD of two numbers

def findgcd(a, b):
    if(b == 0):
        return a
    else:
        return findgcd(b, a % b)

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

gcd = findgcd(num1,num2)
print("GCD of ",num1," & ",num2," is ",gcd)