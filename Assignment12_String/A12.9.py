str = input("Enter a string:")

words = len(str.split())
characters = len(str.replace(" ", ""))

print("Number of words:", words)
print("Number of characters:", characters)