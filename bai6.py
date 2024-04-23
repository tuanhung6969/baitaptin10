A = [1,-2,3,4,5,-9]
def am(A):
    b=[]
    for i in A:
        if i <0:
            b.append(i)
    print(b)
am(A)