import random

words = ['book', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste', 'shirmoz']

# i = random.randint(0, len(words)-1)
# word = words[i]

word = random.choice(words) # clock
joon = 10

answerArr =[]

while joon > 0:
    string = ''
    for i in word:
        if i in answerArr:
            string += (i)
        else:
            string += '- '
    if string == word:
        print('You Win')
        break

    print(string) # - - - - -

    user_character = input().lower() # s

    if user_character in word:

        answerArr.append(user_character)
        
        print('yes')
    else:
        joon = joon - 1
        print('no')

if (joon <= 0):
    print('You Lose')
    
