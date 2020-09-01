#Write a Pyhton program to read email-id from user and sparate the user name and the host name using string slicing ,find, replace method

email = input("Enter email id : ")

for i in range(0,len(email)):
    if "@" == email[i]:
        user_id = email[:i]
        print("User id : "+user_id)
        host = email[i+1:]
        print("Host : "+host)

