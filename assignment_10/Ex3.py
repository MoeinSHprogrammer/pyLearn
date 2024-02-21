class Date:
    
    def __init__(self , y , m ,d) -> None:
        
        self.year = y
        self.month = m
        self.day = d
    
    def SpendDate(self, date):
        
        yday = (date.year - self.year) * 365
        mday = (date.month - self.month) * 30
        dday = (date.day - self.day)
        return (yday + mday + dday)


import datetime

time1 = Date(2023 , 10 , 26)
now = datetime.date.today()
today = Date(now.year,now.month,now.day)

print(time1.SpendDate(today))

