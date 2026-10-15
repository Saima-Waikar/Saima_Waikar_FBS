from threading import Thread
def fun1():
    for i in range(5):
        print("Saima")
def fun2():
    for i in range(5):
        print("Waikar")
t1=Thread(target=fun1)
t2=Thread(target=fun2)
t1.start()
t2.start()
t1.join()
t2.join()
print("I am in Main thread")