from threading import Thread
class demo1(Thread):
    def run(self):
        for i in range(5):
            print("Saima")
class demo2(Thread):
    def run(self):
        for i in range(5):
            print("Waikar")
d1=demo1()
d2=demo2()
d1.start()
d2.start()
