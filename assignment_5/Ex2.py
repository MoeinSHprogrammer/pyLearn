
n = int(input())
m = int(input())

for i in range(n):
    string = ''
    for j in range (m):
            string += (str(i + 1 * j + 1) + str("  "))
    print(string)