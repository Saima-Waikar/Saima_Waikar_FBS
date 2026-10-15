import re

data = "a ab abb abbb"

print(re.findall(r"ab*", data))
print(re.findall(r"ab+", data))
print(re.findall(r"ab?", data))
print(re.findall(r"\d{3}", "12 123 1234"))
print(re.findall(r"\d{2,4}", "1 12 123 1234"))