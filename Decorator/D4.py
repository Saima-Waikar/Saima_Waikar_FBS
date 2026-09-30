#Closure
def outer():
    a = "Virat"
    def inner():
        print(a)
    return inner
x = outer()
x()