import math


a = int(input())
b = int(input())

op = input()

res = None
if op == "+":
    res = a + b

elif op == "-":
    res = a - b

elif op == "/":
    if b != 0:
        res = a / b
    else:
        ('divided by zero')

elif op == "*":
    res = a * b

elif op == "pow":
    res = a ** b

elif op == "sin":
    res = math.sin(a)

elif op == "cos":
    res = math.cos(a)

elif op == "tan":
    res = math.tan(a)

elif op == "cot":
    res = math.cos(a) / math.sin(a)

elif op == "radical":
    res = math.sqrt(a)
    
if res != None:
    print(res)
else:
    print('Wrong Operation!')