def decorator(a):
    print("I am in decorator")
    def innerfun():
        print("Time started ")
        print("Logger added")
        a()
        print("Time Stopeed")
        print("Logger removed ")
    return innerfun 

@decorator
def login():
    print("Log in is Done")

login()
