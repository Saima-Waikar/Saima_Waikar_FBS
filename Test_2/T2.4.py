length = float(input("Enter length of wall: "))
height = float(input("Enter height of wall: "))
rate = float(input("Enter painting cost per sq.ft: "))
area = 4 * length * height
cost = area * rate
print("Total area =", area)
print("Total painting cost =", cost)