feet = float(input("Enter distance in feet: "))
inches = float(input("Enter inches: "))

total_inches = (feet * 12) + inches

meters = total_inches * 0.0254
centimeters = total_inches * 2.54

print(f"Distance in meters = {meters}")
print(f"Distance in centimeters = {centimeters}")