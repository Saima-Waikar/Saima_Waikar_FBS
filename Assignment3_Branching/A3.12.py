num = int(input("Enter a number:"))

a = num // 100
b = (num//10)%10
c = num % 10
reverse = c*100+b*10+a

if(reverse == num):
    print("Number is palindrome")
else:
    print("Number is not palindrome")