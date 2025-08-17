# Find the sum of three-digit number.

num = int(input("enter the digit number:"))
temp = num

d1 = temp % 10
temp  = temp // 10

d2 = temp % 10
temp  = temp // 10

d3 = temp % 10
temp  = temp // 10
sum = (d1 + d2 + d3)

print(f'sum of digit{sum}')
