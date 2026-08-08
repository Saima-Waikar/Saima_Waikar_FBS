gender = input('Enter gender (Male or Female):')
age = int(input('Enter age:'))
if(gender == "Female"):
    if(age >= 18):
        print("Girl is eligible for marriage")
    else:
        print("Girl is not eligible for marriage")
else: 
    if(age >= 21):
        print("Boy is eligible for marriage")
    else:
        print("Boy is not eligible for marriage")