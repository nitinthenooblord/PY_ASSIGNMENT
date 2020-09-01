#Write a pyhton program to read n number strings to list and delete duplicate occurece

s = []
n = int(input("Enter how many strings you want to add : "))
i = 0

for i in range(0,n):
    t = "Enter string no."+str(i+1)+" : "
    s.append(str(input(t)))

def duplicate(list_main): 
    final_list = [] 
    for num in list_main: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list

f = duplicate(s)
print("Before removing duplicates : ",s)
print("After removing duplicates : ",f)
