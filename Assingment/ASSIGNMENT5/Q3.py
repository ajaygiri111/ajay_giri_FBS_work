# Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

num_passenger = int(input("enter number of passengers"))
ticket_cost = int(input("enter ticket cost"))

total_amount = 0

for i in range(1, num_passenger + 3):
    age = int(input("Enter age for passenger:"))
    
    if (age < 12):
        amount = ticket_cost * 0.7 # 30% discount
        print(f"Passenger {i}: Children ticket price. Amount: {amount}")
    elif (age > 59):
        amount = ticket_cost * 0.5 # 50% discount
        print(f"Passenger {i}: Senior citizen ticket price. Amount: {amount}")
    else:
        amount = ticket_cost # full price
        print(f"Passenger {i} (Adult) Ticket Price: {amount}")

        total_amount += amount

print(f"Total amount for all passengers: {total_amount}")
