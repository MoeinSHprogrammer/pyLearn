
a = int(input())
b = int(input())
c = int(input())


if(a<b+c and b<a+c and c<a+b):
    print("Yes, we have triangle.")
else:
    print("No, This is not a triangle.")
