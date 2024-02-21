import qrcode

name = str (input())
phoneNumber = str (input())
img = qrcode.make(name + "|" + phoneNumber)
print(img)
img.save("name_phone.png")