# Write a program to print first n prime numbers.
num = int(input("enter the number of check it prime or not: "))
count = 0
i = 2
while (count < num):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=' ')
        count += 1
    i += 1