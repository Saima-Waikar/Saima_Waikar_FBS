str = input("Enter a string: ")

words = str.split()

unique_words = set()

count = {}

for i in words:

    unique_words.add(i)

    if i in count:

        count[i] = count[i] + 1

    else:

        count[i] = 1

print("Unique words:", unique_words)
print("Frequency:", count)