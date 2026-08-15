correct_id = "admin"
correct_password = "1234"

attempts = 0

while attempts < 3:
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == correct_id and password == correct_password:
        print("Login Successful")
        break
    else:
        print("Incorrect User ID or Password")
        attempts = attempts + 1

if attempts == 3:
    print("You have used all 3 attempts. Program terminated.")