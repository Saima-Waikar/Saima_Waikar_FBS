def decore(a):
    print("I am in decorer")
    def innerfun():
        print("Time started ")
        print("Logger added")
        a()
        print("Time Stopeed")
        print("Logger removed ")
    return innerfun 

@decore
def login():
    print("Log in is Done")
    
@decore
def logout():
    print("Logout in is Done")

login()
logout()