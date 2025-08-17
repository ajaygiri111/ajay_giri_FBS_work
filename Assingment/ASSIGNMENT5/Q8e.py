# x - x2/3 + x3/5 - x4/7 + .... to n terms

x = float(input("Enter the value of x "))
n = int(input("Enter the number of terms "))
S = 0
for i in range(n):
    term = ((-1) ** i) * (x ** (i + 1)) / (2 * i + 1)
    S += term
print("The sum of the series is:", S)