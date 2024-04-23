#bài 4 ..hùng

A = [2,4,6,1,3,9,0]
def chan(A):
    b =[]
    for i in A:
        if i%2==0:
            b.append(i)
    print(len(b))

chan(A)