class time:
    def __init__(self,hr,min,sec):
        self.hr = hr
        self.min = min
        self.sec = sec
    def __str__(self):
        return f"{self.hr}:{self.min}:{self.sec}"
    def __add__(self,other):
        thr = self.hr + other.hr
        tmin = self.min + other.min
        tsec = self.sec + other.sec
        t = time(thr,tmin,tsec)
        return t
t1 = time(12,40,6)
t2 = time(15,8,90)
print(t1+t2)