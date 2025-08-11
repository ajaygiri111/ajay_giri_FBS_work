# 5. Write a program to enter P, T, R and calculate Compound Interest.
p = float(input("enter principal amount"))
t = float (input("enter the time in year"))
R = (input("enter the annual rate of intest"))

CI = p*((1+ R / 100) ** t) - p

print(f'compund intrest is:{CI}')


