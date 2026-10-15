f = None
try:
    f = open("abc.txt", "r")
    data = f.read
    if not data:
        raise Exception("File is empty")
except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)
else:
    print(data)
finally:
    if f is not None:
        print("File closed")
        f.close()
print("All task are completed")
