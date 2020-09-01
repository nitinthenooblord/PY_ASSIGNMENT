#Write a Pyhton program to enter binary number and convert it into decimal number

def binaryToDecimal(binary): 
    decimal, i = 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    print(decimal)

num = int(input("Enter binary number : "))
binaryToDecimal(num)