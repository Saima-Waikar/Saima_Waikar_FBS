with open(r"D:\FBS\Core python\Demos\Basics\file\abc.txt", "w") as f:
    f.write("Good Morning")

with open(r"D:\FBS\Core python\Demos\Basics\file\abc.txt", "r") as f:
    data = f.read()
    print(data)

with open(r"D:\FBS\Core python\Demos\Basics\file\abc.txt", "a") as f:
    f.write("Good Evening")