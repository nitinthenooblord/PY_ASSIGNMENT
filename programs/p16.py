#Write a python program to read multiple lines and split each of word using list split and find the occurrence of each word

s = input("Enter line : ")
list_of_line = s.split(" ")

all_freq = {} 
for i in list_of_line: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1

print ("\nCount of all words :\n"+str(all_freq))

