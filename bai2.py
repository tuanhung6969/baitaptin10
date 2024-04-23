#bài 2 

print("ax² + bx + c = 0")


a = int(input("type a "))
b = int(input("type b "))
c = int(input("type c "))

print("phương trình :", a,"x² + ", b,"x + ", c, " = 0")
def giaipt(a,b,c):
    z = 2*a
    delta = b*b -4*a*c
    if delta < 0:
        print("phương trình vô nghiệm")
    if delta ==0:
        x = -b/z
        print("x1 = x2 =", x)

    if delta > 0 :
        n = delta**(1/2)
        x1 = (-b + n)/z
        x2 = (-b - n)/z
        print(x1)
        print(x2)


if a !=0:
    giaipt(a,b,c)
if a ==0:
    print("pt vô ng")