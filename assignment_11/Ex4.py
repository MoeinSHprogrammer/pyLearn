n = int(input())

if n % 2 == 0:
    print("adad joz ast va nemitavan farsh sakht")

elif n % 2 == 1 and n > 0:
    
    carpet = []
    finalCarpet = []

    cElement = int(((n - 1) / 2))
    a = 1
    b = n - 1
    c = 1

    for i in range(n):
        line = []
        for j in range(n):
            line.append(cElement)
        carpet.append(line)
    finalCarpet.append(carpet[0])
    for i in range(n):
        temp = []
        for z in finalCarpet[i]:
            temp.append(z)
        if a >= b:
            break
        for j in range(a , b):
            temp[j] -= c
        a += 1
        b -= 1
        finalCarpet.append(temp)

    for i in range (len(finalCarpet) - 2 , -1 , -1):
        finalCarpet.append(finalCarpet[i])

for i in finalCarpet:
    print(i)