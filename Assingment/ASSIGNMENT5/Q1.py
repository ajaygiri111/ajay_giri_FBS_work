correct_userid = "admin"
correct_password = "12345"

for attempt in range(1, 4):
    userid = input("Enter userid")
    password = input("Enter password")
    if(userid == correct_userid and password == correct_password):
        print("Login successful!")
        break
    else:
        print("Incorrect userid or password. Try again.")