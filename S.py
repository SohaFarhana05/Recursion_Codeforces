import sys
sys.setrecursionlimit(10**7)
def fun(i,arr):
    if i<0:
        return 0
    return arr[i] + fun(i-1,arr)
t = int(input())
l = list(map(int,input().split()))
avg = fun(t-1,l)/t
print(f"{avg:.6f}")