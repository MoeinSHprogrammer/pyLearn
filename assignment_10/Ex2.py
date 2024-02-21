class Time:
    
    def __init__(self , h , m ,s) -> None:
        
        self.hours = h
        self.minutes = m
        self.second = s
    
    def ToSecond(self):
        
        return (self.hours * 3600 + self.minutes * 60 + self.second)


time1 = Time(2 , 30 , 26)

print(time1.ToSecond())