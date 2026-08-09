days = int(input('Enter Days:'))

years = days//365
days = days % 365

weeks = days//7
days = days % 7

print(f'Years = {years}, Weeks = {weeks} and Days = {days}')