m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))

t = m1+m2+m3+m4+m5
p = (t)/500*100

print(f"Total marks ={t}")
print(f"Percentage = {p}%")

if(p>=75):
    print("Distinction")
elif(p>=60):
    print("First class")
elif(p>=50):
    print("Second class")
elif(p>=35):
    print("Pass class")
else:
    print("Fail")
