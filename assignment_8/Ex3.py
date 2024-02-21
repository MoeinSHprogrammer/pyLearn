def ReadFile():
    global wordsBank
    f = open("assignment_8/Translate.txt" , "r")
    temp = f.read().split("\n")
    f.close()
    wordsBank = []
    for i in range (0 , len(temp), 2):
        dic = {
            "en": temp[i],
            "fa": temp[i+1]
        }

        wordsBank.append(dic)

def ShowMenu():
    print("wellcome to translator")
    print("1 - press 1 to en to fa translate")
    print("2 - press 2 to fa to en translate")
    print("3 - press 3 to add new word to dictionary")
    print("4 - press 4 to exit")

def TranslateEnToFa():

    userInput = input("Enter your english text: ").split(" ")
    output = ""
    for userWord in userInput:
        for word in wordsBank:
            if userWord == word["en"]:
                output += (word["fa"] + " ")
                break
        else:
            output += (userWord + " ")

    print(output)

def TranslateFaToEn():
    userInput = input("Enter your farsi text: ").split(" ")
    output = ""
    for userWord in userInput:
        for word in wordsBank:
            if userWord == word["fa"]:
                output += (word["en"] + " ")
                break
        else:
            output += (userWord + " ")

    print(output)

def AddWordToDic():
    en = input("enter english word: ")
    fa = input("enter farsi word: ")
    dic = {
        "en": en,
        "fa": fa
        }
    wordsBank.append(dic)

ReadFile()
ShowMenu()
choice = int(input("adad mored nazar ra vared konid: "))

if choice == 1:
    TranslateEnToFa()
elif choice == 2:
    TranslateFaToEn()
elif choice == 3:
    AddWordToDic()
elif choice == 4:
    with open("assignment_8\Translate.txt", 'w') as f:
        for word in wordsBank:
            f.writelines(word["en"])
            f.writelines(word["fa"])
    f.close()
    exit(0)

