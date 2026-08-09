h = int(input('Enter Hours:'))
m = int(input('Enter Minutes:'))
s = int(input('Enter Seconds:'))

total_seconds = (h * 60 * 60) + (m * 60) + (s)

print(f'Total Seconds are {total_seconds}')