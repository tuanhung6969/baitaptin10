#bài 5


n = int(input())
def prime(n):
    C = 0
    k =1
    while k<n :
        if n%k ==0:
            C = C+1
        k= k +1
    if C==1:
        return True
    else:
        return False
for k in range(1, n+1):
    if prime(k):
        print(k, end=" ")