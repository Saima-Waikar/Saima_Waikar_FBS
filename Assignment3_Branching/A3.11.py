total = 0
for i in range(1,6):
    age = int(input("Enter age:"))
    amount = float(input("Enter amount:"))
    if(age<=12):
        amount = amount - (amount*30/100)
    elif(age<=59):
        amount = amount - (amount*50/100)
total = total + amount
print("Total ticket amount =", total)
