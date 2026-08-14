l = int(input("Enter length of rectangle:"))
b = int(input("Enter breadth of rectangle:"))
r = int(input("Enter radius of circle:"))
area_rectangle = l * b
area_circle = (3.14*r*r)/2
area = area_rectangle + area_circle
perimeter_circle = 3.14*r + 2*r
perimeter_rectangle = 2*(l+b)
perimeter = perimeter_rectangle + perimeter_circle 
print(f"Area is {area}")
print(f"Perimeter is{perimeter}")
