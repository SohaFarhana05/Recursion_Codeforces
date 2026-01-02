def f(n,k):
    if n==0:
        return 
    
    h = ' '*(k-n) + '*' * (2*n-1)
    print(h)
    f(n-1,k)
n = int(input())
f(n,n)