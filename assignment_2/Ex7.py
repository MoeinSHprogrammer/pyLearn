
n = int(input('enter len: '))

first = 0
secend = 1
buf = 0
print(1)
for i in range(n-1):
    print(first + secend)
    buf = first + secend

    first = secend
    secend = buf
