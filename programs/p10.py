#Write a Python program to search a character in a given string using slicing

s = input("Enter string : ")
c = input("Enter a search character : ")

flag = 0
for i in range(0,len(s)-1):
    if c == s[i]:
        print("Given charcter found at the position index ",i," in String "+s)
        flag = 1

if flag == 0:
    print("Given charcter not found")
