num = int(input("Enter a three-digit number: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

sum = a + b + c

print(f"Sum of digits = {sum}")