#Write a Python program find the accurence of each character in string (Slicing)

test_str = "deevil" 
all_freq = {} 
for i in test_str: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1

print ("Count of all charactersis\n"+str(all_freq))