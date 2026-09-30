def outer():
    print("I am in outer function")
    def inner():
        print("I am in inner function")
    return inner
x = outer()
x()