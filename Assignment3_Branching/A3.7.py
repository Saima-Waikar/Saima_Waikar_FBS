userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid User ID or Password")