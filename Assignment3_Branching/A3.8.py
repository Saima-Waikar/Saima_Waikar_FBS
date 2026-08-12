userid = input("Enter User ID: ")
password = input("Enter Password: ")

if (userid == "admin" and password == "1234"):
    num = 5832
    print("Captcha:", num)

    n = int(input("Enter given Captcha: "))

    if n == num:
        print("Success")
    else:
        print("Failed")
else:
    print("Invalid User ID or Password")