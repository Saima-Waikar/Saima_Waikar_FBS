#import math                               ###with math library
#a = float(input('Enter a :'))
#b = float(input('Enter b :'))
#c = float(input('Enter c :'))

#d = b*b-4*a*c
#x1 = (-b + math.sqrt(d))/(2*a)
#x2 = (-b - math.sqrt(d))/(2*a)

#print(f'Root1 of Quadratic equation is{x1}')
#print(f'Root2 of Quadratic equation is{x2}')



a = float(input('Enter a :'))             ###without math library - use 0.5 for sqrt 
b = float(input('Enter b :'))
c = float(input('Enter c :'))

d = b*b-4*a*c
x1 = (-b + d**0.5)/(2*a)
x2 = (-b - d**0.5)/(2*a)

print(f'Root1 of Quadratic equation is{x1}')
print(f'Root2 of Quadratic equation is{x2}')