
var = 0
counter = 0

while(1):
    inp = input()
    if inp == 'exit':
        break
    else:
        counter += 1
        var += int(inp)
print(var/counter)