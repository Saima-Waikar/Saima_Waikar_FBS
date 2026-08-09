p = int(input('Enter Principle:'))
r = float(input('Enter Rate:'))
t = int(input('Enter Time(Year):'))

compound_interest = p * (1 + r / 100) ** t - p

print(f'Simple Interest is {compound_interest}')