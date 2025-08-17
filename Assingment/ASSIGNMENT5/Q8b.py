# N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

num = int(input("enter a number"))

total = 0
for i in range(1, num + 1):
    total += num ** i 

print("the sum of the series is:",total)