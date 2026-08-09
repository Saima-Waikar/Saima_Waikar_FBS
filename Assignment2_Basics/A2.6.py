basic = float(input("Enter basic salary: "))

da = 10 / 100 * basic
ta = 12 / 100 * basic
hra = 15 / 100 * basic

total_salary = basic + da + ta + hra

print(f"DA = {da}")
print(f"TA = {ta}")
print(f"HRA = {hra}")
print(f"Total salary = {total_salary}")