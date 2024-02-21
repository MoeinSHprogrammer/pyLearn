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

kasr1 = Fraction(2, 3)
kasr2 = Fraction(4, 5)
print(kasr1.jam(kasr2).soorat / kasr1.jam(kasr2).makhraj)
print(kasr1.tafrigh(kasr2).soorat / kasr1.tafrigh(kasr2).makhraj)
print(kasr1.zarb(kasr2).soorat / kasr1.zarb(kasr2).makhraj)
print(kasr1.taqsim(kasr2).soorat / kasr1.taqsim(kasr2).makhraj)