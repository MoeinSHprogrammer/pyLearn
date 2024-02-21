
n = int(input())
counter = n
for i in range(n):
    print(counter*" "+ ((2*i)+1)*"*")
    counter -= 1
counter = 1
for i in range(n-1 , -1, -1):
    print(counter*" "+ ((2*i)+1)*"*")
    counter += 1