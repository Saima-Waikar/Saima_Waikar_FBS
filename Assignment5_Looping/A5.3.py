passenger = int(input("Enter number of passengers:"))
ticket = int(input("Enter per tickect cost:"))
for i in range(1,passenger+1):
    age = int(input(f"Enter age of passenger{i}:"))
    i +=1
if(age<12):
    cost = ticket - ((ticket*30)/100)
if(age>59):
    cost = ticket - ((ticket*50)/100)
else:
    cost = 0
total_amount = ticket + cost 
print(f"Total amount is {total_amount}")