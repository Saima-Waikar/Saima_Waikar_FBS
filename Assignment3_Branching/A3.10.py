gender = input("Enter Gender(F/M):")
age = int(input("Enter age:"))
if(gender=='F' and age>=18):
    print("Eligible")
elif(gender=='M' and age>=21):
    print("Eligible")
else:
    print("Not Eligible")
