# Write a program to solve the following series :
## a. 1! + 2! + 3! + 4! + .....n!

num = int(input("enter a number"))

total = 0
fact = 1

for i in range(1, num + 1): 
    fact *= i  # Calculate factorial
    total += fact  # Add factorial to total

print("The sum of the series is:", total)