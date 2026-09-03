dict = {1: 'A', 2: 'B', 3:'C', 4:'D'}
mul_dig = 1
mul_str = ""
for i in dict:
    mul_dig = i * mul_dig
    mul_str = i * mul_str
print(mul_dig)
print(mul_str)