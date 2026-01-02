def f(n,k):
    if n==0:
        return 
    f(n-1,k)
    h = ' '*(k-n) + '*' * (2*n-1)
    print(h)
n = int(input())
f(n,n)