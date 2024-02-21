x = int(input())
y = int(input())

if x > y:
    gcd_ = x
else:
    gcd_ = y

for i in range (gcd_ , 1, -1):
    if((x % gcd_ == 0) and (y % gcd_ == 0)):
           break
    gcd_ -= 1

print(gcd_)


