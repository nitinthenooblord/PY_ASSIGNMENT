# 02. Write a Pyhton program to generate a prime between 2 to 20

end = 20

for j in range(2, end):
    if j > 1:
        for i in range(2, j):
            if (j % i) == 0:
                break
        else:
            print(j)