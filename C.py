def f(i):
    if i==1:
        print(1, end = '')
        return 
    print(i , end = " ")
    f(i-1)
n = int(input())
f(n)