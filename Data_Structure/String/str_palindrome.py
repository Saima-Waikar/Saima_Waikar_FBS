str = 'racecar'
rev_str = ''

for char in str:
    rev_str = char + rev_str
if(str == rev_str):
    print('The string is palindrome')
else:
    print('The string is not palindrome')