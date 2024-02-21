

sec = int(input())

h = int(sec / 3600)

sec = sec % 3600

m = int(sec / 60)

s = sec % 60

if h < 10:
    h = '0' + str(h)
if m < 10:
    m = '0' + str(m)
if s < 10:
    s = '0' + str(s)

print(str(h) + ":" + str(m) + ":" + str(s))