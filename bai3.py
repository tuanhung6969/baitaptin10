#bài 3
A= [1,-1,-2,-3,4]
def tongam(A):
    x=0
    for i in A:
        if i < 0:
            x = x+i
    print(x)
tongam(A)