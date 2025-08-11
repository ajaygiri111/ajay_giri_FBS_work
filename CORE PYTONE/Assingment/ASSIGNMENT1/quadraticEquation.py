# Program to Find the Roots of a Quadratic Equation
a = int(input("enter value for a:"))
b = int(input("enter value for b:"))
c = int(input("enter value for c:"))
sqrt = ((b**2))-((4*a*c))**0.5
res1 = (-b+sqrt)/2*a 
res2 = (-b-sqrt)/2*a

print(f"result 1 {res1}")
print(f"result 2 {res2}")