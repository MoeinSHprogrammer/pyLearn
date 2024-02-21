
n = int(input())
m = int(input())

for i in range(n):
    string = ''
    for j in range (m):
        if (j + i) %2 == 0:
            string += '*'
        else:
            string += "#"
    print(string)