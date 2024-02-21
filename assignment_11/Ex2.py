class Time:
    
    def __init__(self , h , m ,s) -> None:
        
        self.hours = h
        self.minutes = m
        self.second = s

    def jam(self , time):

        s = self.second + time.second

        m = self.minutes + time.minutes

        h = self.hours + time.hours

        if s > 59:
            s -= 60
            m += 1
        if m > 59:
            m -= 60
            h += 1
        if h > 24:
            h -= 24

        return(Time (h , m , s))

    def tafriq(self , time):
        if self.hours > time.hours:
            h = self.hours - time.hours
            m = self.minutes - time.minutes
            if m < 0:
                h -= 1
                m += 60
            s = self.second - time.second
            if s < 0:
                m -= 1
                s += 60

        else:
            h = time.hours - self.hours
            m = time.minutes - self.minutes
            if m < 0:
                h -= 1
                m += 60
            s = time.second - self.second
            if s < 0:
                m -= 1
                s += 60
        return (Time(h, m, s))


    def ToSecond(self):
        
        return (self.hours * 3600 + self.minutes * 60 + self.second)
    
    def gmtTotehran(self):
        t1 = self.jam(Time(4,30,00))
        if t1.second > 59:
            t1.second -= 60
            t1.minutes += 1
        if t1.minutes > 59:
            t1.minutes -= 60
            t1.hours += 1
        if t1.hours > 24:
            t1 = t1.tafriq(Time(24,0,0))
        return (t1)

    
    def printTime(self):
        print(self.hours,":",self.minutes ,":",self.second)

def secondTotime(self):
        
    h = int(self/3600)
    m = int((self % 3600) / 60)
    s = (self % 3600) % 60
    return Time(h , m , s)

time1 = Time(2 , 33 , 50)
time2 = Time (3, 12, 24)

jam = time1.jam(time2)
tafriq = time1.tafriq(time2)
toTime = secondTotime(1212)
gTot = time1.gmtTotehran()


jam.printTime()
tafriq.printTime()
print(time1.ToSecond())
toTime.printTime()
gTot.printTime()



