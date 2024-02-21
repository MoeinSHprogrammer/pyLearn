
n = int(input('enter snake len: '))
snake = ''

for i in range(n):
    if i%2 == 0:
        snake += '*'
    else:
        snake += '#'

print(snake)

            
