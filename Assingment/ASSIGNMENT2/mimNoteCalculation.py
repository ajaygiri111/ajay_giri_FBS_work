# Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount.
amount = int(input("enter the amount to calculate min no of amount"))

temp = amount
two_thousand = temp // 2000
temp = temp % 2000

five_hundred = temp // 500
temp = temp % 500

two_hundred = temp // 200
temp = temp % 200

hundred = temp // 100 
temp = temp % 100

fifty = temp // 50
temp = temp % 50

twenty = temp // 20
temp = temp % 20

ten = temp // 10
temp = temp % 10

print(f'2000:{two_thousand},\n 500:{five_hundred},\n 200:{two_hundred},\n 100:{hundred},\n 50:{fifty},\n 20:{twenty},\n 10:{ten}')