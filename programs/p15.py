#Write a python program to read the email id'email of n users and create a list of user id's

email = []
user_id = []
n = int(input("Enter how many strings you want to add : "))
i = 0

for i in range(0,n):
    t = "Enter string no."+str(i+1)+" : "
    email.append(str(input(t)))

for i in range(0,len(email)):
    s = email[i]
    for j in range(0,len(s)):
        if "@" == s[j]:
               user_id.append(s[:j])

print("List of user id : ",user_id)