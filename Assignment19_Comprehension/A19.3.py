# 3. Count the number of spaces in a string (take input from user)

text = input("Enter a string: ")

spaces = [i for i in text if i == " "]

print("Number of spaces:", len(spaces))