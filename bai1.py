a = int(input())
b = int(input())
def giaipt(a,b):
    if a ==0:
        if b == 0:
            print("pt có mọi nghiệm")
        else :
            print("pt vô nghiệm")
    else :
        c= -b/a
        print("pt có nghiệm"+ str(c) )

giaipt(a,b)