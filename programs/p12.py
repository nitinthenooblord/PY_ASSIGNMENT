#Write a Python Program to read String from user and write a function to calculate the lenght of string

s = input("Enter a String : ")

def lenght(s):
    count = 0
    while s[count:]: 
        count += 1
    return count

print("Lenth of string is : ",lenght(s))