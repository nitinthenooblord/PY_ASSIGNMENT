 #Write a Python program to enter decimal number and calculate and display binary eqyivalent of this number

def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

dec = int(input("Enter number : "))
convertToBinary(dec)
print()