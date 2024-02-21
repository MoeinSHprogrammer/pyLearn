n = int(input())

fac = 1
for i in range (1 , n):
    fac *= i

    if (fac == n):
        print ('yes')
        break
    elif (fac > n):
        print('No')
        break