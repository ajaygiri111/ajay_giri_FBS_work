# Find the sum of a geometric series from 1 to n where the common ratio is 2.
num = int(input("enter the number "))
total = 0
for i in range(num + 1):
    total += 2 ** i
print("The sum of the geometric series is:", total)