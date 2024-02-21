h = input()

hour = int(h[0]+h[1])
minutes = int(h[3]+h[4])
second = int(h[6]+h[7])

print(3600 * hour + 60 * minutes + second)
