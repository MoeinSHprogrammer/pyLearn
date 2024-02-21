import qrcode
PRODUCTS = []

def ReadFromDB():
    
    f = open("assignment_7\database.txt" , "r")
    for line in f:
        
        result = line.split(",")
        my_dic = {"code": result[0] , "name": result[1] , "price": result[2] , "count": result[3]}
        PRODUCTS.append(my_dic)
    f.close()

def ShowMenu():
    print("1 - Add")
    print("2 - Edit")
    print("3 - Remove")
    print("4 - Search")
    print("5 - Show List")
    print("6 - Buy")
    print("7 - Exit")

def Add():
    code = input("enter code: ")
    name = input("enter name: ")
    price = input("enter price: ")
    count = input("enter count: ")
    newProduct = {"code": code,"name": name,"price": price,"count": count }
    PRODUCTS.append(newProduct)
def Edit():
    itemCode = int(input("code kala ra vared konid: "))
    changeNum = int(input("Che bakhshi ra taqir midahid\n1-name\n2-price\n3-count\n"))
    newEntery = input("meqdar jadid ra vared konid: ")

    if changeNum == 1:
        item = "name"
    elif changeNum == 2:
        item = "price"
    elif changeNum == 3:
        item = "count"
    for product in PRODUCTS:
        if int(product["code"]) == itemCode:
            product[item] = newEntery
    print("Edit ba movafaqiat anjam shod")
def Remove():
    itemCode = int(input("code kala ra vared konid: "))
    for product in PRODUCTS:
        if int(product["code"]) == itemCode:
            PRODUCTS.remove(product)
    print("Remove ba movafaqiat anjam shod")
def Search():
    userInput = input("Enter your keyword")
    for product in PRODUCTS:
        if product["code"] == userInput or product["name"] == userInput:
            print(product["code"], "\t\t",product["name"], "\t\t",product["price"])
            break
        else:
            print("not found")
def ShowList():
    print("code\t\tname\t\tprice")
    for product in PRODUCTS:
        print(product["code"], "\t\t",product["name"], "\t\t",product["price"])

def Buy():
    buyItems = []
    def showFactor():
        sumation = 0
        print("code\t\tname\t\tprice")
        for product in buyItems:
            print(product["code"], "\t\t",product["name"], "\t\t",(int(product["price"]) * int(product["count"])))
            sumation += (int(product["price"]) * int(product["count"]))
        print("mablaq qabel pardakht : ", sumation)


    while(1):
        boolianParameter = input("aya hanooz kharid darid: y or n: \n")
        if boolianParameter == "y":
            itemCode = int(input("code kala ra vared konid: "))
            for product in PRODUCTS:
                if int(product["code"]) == itemCode:
                    itemCount = int(input("tedad ra vared konid: "))
                    if int(product["count"]) >= itemCount:
                        dic = {"code": product["code"] , "name": product["name"] , "price": product["price"] , "count": itemCount}
                        buyItems.append(dic)
                        product["count"] = str(int(product["count"]) - itemCount)
                        if int(product["count"]) <= 0:
                            PRODUCTS.remove(product)
                    else:
                        print("mojudi kala kafi nist")
        else:
            showFactor()
            break

        
def QrMaker():
    itemCode = int(input("code kala ra vared konid: "))
    for product in PRODUCTS:
        if int(product["code"]) == itemCode:
            img = qrcode.make(str(product["code"]) + "|" + str(product["name"]) + "|",str(product["price"]))
            img.save("productDetails.png")


print("Wellcome to my store")
print("Loading ...")

ReadFromDB()
print("Data Loaded")
while(1):
    ShowMenu()
    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        Add()
    elif choice == 2:
        Edit()
    elif choice == 3:
        Remove()
    elif choice == 4:
        Search()
    elif choice == 5:
        ShowList()
    elif choice == 6:
        Buy()
    elif choice == 7:
        with open("assignment_7\database.txt", 'w') as f:
            for product in PRODUCTS:
                f.writelines(product["code"] +","+ product["name"] +","+ product["price"] +","+ product["count"])
        f.close()
        exit(0)
    else:
        print("mesl adam vared kon")

