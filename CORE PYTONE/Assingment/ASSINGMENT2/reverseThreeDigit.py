num = int(input("enter the digit"))

hunderd = num // 100
tens = (num // 10) % 10
ones = num % 10

reversed = (ones * 100) + (tens * 10) + hunderd
print(f'reverse number is {reversed}')