#Write a Pyhton to accept the user id (n number) sperate the id with host name and return it to the main function

def sparator(email):
    for i in range(0,len(email)):
        if "@" == email[i]:
            user_id = email[:i]
            print("User id : "+user_id)
            host = email[i+1:]
            print("Host : "+host)


while 1:
    print("To quit type exit\n")
    email = input("Enter email id : ")
    if email == "exit":
        break
    else:
        sparator(email)
        print()