# 6. Use a dictionary comprehension to count the length of each word in a sentence (take input from user)

text = input("Enter a sentence: ")

words = text.split()

result = {i: len(i) for i in words}

print(result)