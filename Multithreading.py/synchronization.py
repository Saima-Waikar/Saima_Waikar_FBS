from threading import Thread, Lock

l = Lock()

def display(name):
    l.acquire()

    for i in range(3):
        print(name)

    l.release()

t1 = Thread(target=display, args=("Saima",))
t2 = Thread(target=display, args=("Waikar",))

t1.start()
t2.start()