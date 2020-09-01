#Write a Python program to count the number of digits in a given number

num = int(input("Enter number : "))

length = 0
while(num > 0):  
    num = num // 10
    length += 1

print(length)