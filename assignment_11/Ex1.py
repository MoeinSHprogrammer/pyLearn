class Fraction:
    def __init__(self , s , m):
        self.soorat = s
        self.makhraj = m
    
    def jam(self , kasr):
        
        return (Fraction(((self.makhraj * kasr.soorat)+(kasr.makhraj * self.soorat)) , (self.makhraj * kasr.makhraj)))
    def tafrigh(self, kasr):
        return (Fraction(((self.makhraj * kasr.soorat)-(kasr.makhraj * self.soorat)) , (self.makhraj * kasr.makhraj)))
    def zarb(self, kasr):
        return (Fraction((self.soorat * kasr.soorat) , (self.makhraj * kasr.makhraj)))
    def taqsim(self, kasr):
        return (Fraction((self.soorat * kasr.makhraj) , (self.makhraj * kasr.soorat)))
    def kasr_to_adad(self):
        return (self.soorat / self.makhraj)
    def sade_sazi(self):
        x = self.soorat
        y = self.makhraj

        if x > y:
            gcd_ = x
        else:
            gcd_ = y

        for i in range (gcd_ , 1, -1):
            if((x % gcd_ == 0) and (y % gcd_ == 0)):
                break
            gcd_ -= 1

        return Fraction(self.soorat / gcd_ , self.makhraj / gcd_)




kasr1 = Fraction(4, 10)
kasr2 = Fraction(4, 5)
print(kasr1.jam(kasr2).soorat / kasr1.jam(kasr2).makhraj)
print(kasr1.tafrigh(kasr2).soorat / kasr1.tafrigh(kasr2).makhraj)
print(kasr1.zarb(kasr2).soorat / kasr1.zarb(kasr2).makhraj)
print(kasr1.taqsim(kasr2).soorat / kasr1.taqsim(kasr2).makhraj)
print(kasr1.kasr_to_adad())
print(kasr1.sade_sazi().soorat , "/" , kasr1.sade_sazi().makhraj)