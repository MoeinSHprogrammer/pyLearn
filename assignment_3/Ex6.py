x = int(input())
y = int(input())

if x > y:
    lcm = x
else:
    lcm = y

for i in range (lcm , 1, -1):
    if((x % lcm == 0) and (y % lcm == 0)):
           break
    lcm += 1

print(lcm)


