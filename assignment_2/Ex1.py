import random

secretNumber = random.randint(1, 100)
win = False
predictNumber = 0
while (not win):
    guessNumber = int(input())
    predictNumber += 1
    
    if (guessNumber < secretNumber):
        print("Go higher!!")
    if (guessNumber > secretNumber):
        print("Go lower!!")
    if (guessNumber == secretNumber):
        print(f"You win after {predictNumber} guesses")
        win = True