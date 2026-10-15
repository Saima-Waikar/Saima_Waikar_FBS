import re

print(re.findall(r"^Hello", "Hello Saima"))
print(re.findall(r"world$", "Hello world"))
print(re.findall(r"cat|dog", "cat and dog"))
print(re.findall(r"(ab)+", "abab ab"))
print(re.findall(r"(\w)\1", "book coffee"))