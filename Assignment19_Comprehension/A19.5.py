# 5. Find all of the words in a string that are less than 5 letters (take input from user)

text = input("Enter a string: ")

words = [i for i in text.split() if len(i) < 5]

print(words)