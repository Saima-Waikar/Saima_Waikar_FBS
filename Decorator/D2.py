def fun(a):
    a()
def demo():
    print("I am in demo")
x = demo
fun(x)