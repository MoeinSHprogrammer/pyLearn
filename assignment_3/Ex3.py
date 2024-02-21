

n = int(input('enter array len: '))
arr = []
notSortedBool = False
for i in range(n):
    arr.append(input())

for i in range(n):
    for j in range(i,n):
        if arr[i] > arr[j]:
            notSortedBool = True
            break

if notSortedBool:
    print('Not Sorted')
else:
    print('Sorted')
            
