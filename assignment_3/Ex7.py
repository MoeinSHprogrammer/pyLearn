
string = str (input('Enter Your Sentences: '))
count = 1
for i in string:
    if (i == ' '):
        count += 1

print(count)