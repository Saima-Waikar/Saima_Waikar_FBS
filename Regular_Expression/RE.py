import re

data = "Hello Saima 123.abc@gmail.com"

print("Digits:", re.findall(r"\d", data))
print("Complete numbers:", re.findall(r"\d+", data))
print("Non-digits:", re.findall(r"\D+", data))
print("Word characters:", re.findall(r"\w+", data))
print("Non-word characters:", re.findall(r"\W", data))
print("Whitespace:", re.findall(r"\s", data))
print("Non-whitespace:", re.findall(r"\S+", data))
print("Dots:", re.findall(r"\.", data))
print("Any character:", re.findall(r".", data))
print("Words starting at boundaries:", re.findall(r"\b\w+", data))
print("S followed by any 2 char followed by a", re.findall(r"S...a", data))

# Newline example
data1 = "Hello\nSaima"
print("Newline:", re.findall(r"\n", data1))

# Tab example
data2 = "Hello\tSaima"
print("Tab:", re.findall(r"\t", data2))