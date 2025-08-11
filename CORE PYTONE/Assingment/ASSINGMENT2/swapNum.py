# Write a program to swap two numbers using third variable.
x = int(input("enter value of x:"))
y = int(input("enter value of y:"))

z = x
x = y
y = z

print(f'x:{x},\n y:{y}.')