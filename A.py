def f(i):
    if i==0:
        return 
    f(i-1)
    print("I love Recursion")
n = int(input())
f(n)