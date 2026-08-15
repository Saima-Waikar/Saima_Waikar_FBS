n = int(input("Enter number of students: "))

total_percentage = 0

for i in range(n):
    print("\nStudent", i + 1)

    m1 = float(input("Enter marks of subject 1: "))
    m2 = float(input("Enter marks of subject 2: "))
    m3 = float(input("Enter marks of subject 3: "))
    m4 = float(input("Enter marks of subject 4: "))
    m5 = float(input("Enter marks of subject 5: "))

    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    print("Percentage =", percentage, "%")

    total_percentage = total_percentage + percentage

average = total_percentage / n

print("\nAverage Percentage =", average, "%")