# Write a program to reverse three-digit number.

num = int(input("enter the digit number:"))
temp = num

d1 = temp % 10
temp  = temp // 10

d2 = temp % 10
temp  = temp // 10

d3 = temp % 10
temp  = temp // 10
sum = (d1 + d2 + d3)

print(f'D1 {d1}, D2 {d2}, D3 {d3}.')
