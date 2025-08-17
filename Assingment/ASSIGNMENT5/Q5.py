# Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount. (Use looping to optimize
# the problem)

amount = int(input("enter the amount"))

notes = [500, 200, 100, 50, 20, 10, 5]  # List of notes in descending order

print("Minimum notes needed:")
for note in notes:
    count = amount // note       
    amount = amount % note       
    print(f"{note}: {count}")