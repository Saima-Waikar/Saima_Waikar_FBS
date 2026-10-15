f = None
try:
    f = open(r"D:\FBS\Core python\Demos\Basics\file\abc.txt", "r")
    data = f.read
except Exception as e:
    print(e)
else:
    print(data)
finally:
    if f is not None:
        print("File closed")
        f.close()
print("All task are completed")
