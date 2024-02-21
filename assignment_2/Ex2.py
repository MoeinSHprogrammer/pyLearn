import random


computerScore = 0
UserScore = 0
while (1):
    x = random.randint(1,3)

    if x == 1:
        computerChoice = "rock"
    if x == 2:
        computerChoice = "paper"
    if x == 3:
        computerChoice = "scissors"

    y = int(input("1 : rock\n2 : paper\n3 : scissors\nyour Choice: "))

    if x == y:
        print("moosavi")
    elif x == 1 and y == 2:
        UserScore += 1
    elif x == 1 and y == 3:
        computerScore += 1
    elif x == 2 and y == 1:
        computerScore += 1
    elif x == 2 and y == 3:
        UserScore += 1
    elif x == 3 and y == 1:
        UserScore += 1
    elif x == 3 and y == 2:
        computerScore += 1
    print(f"computer Score : {computerScore} \n2user Score : {UserScore}")

    if computerScore == 4:
        print('computer win')
        break
    if UserScore == 4:
        print("you win")
        break

