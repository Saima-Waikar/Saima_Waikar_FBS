class time:
    def __init__(self,hr,min,sec):
        self.hr = hr
        self.min = min
        self.sec = sec

    def __str__(self):
        return f"{self.hr}:{self.min}:{self.sec}"

    def __add__(self,other):
        tsec = self.sec + other.sec
        addmin = tsec // 60
        tsec = tsec % 60

        tmin = self.min + other.min + addmin
        addhr = tmin // 60
        tmin = tmin % 60

        thr = self.hr + other.hr + addhr

        return time(thr,tmin,tsec)

t1 = time(12,40,6)
t2 = time(15,8,90)

print(t1+t2)