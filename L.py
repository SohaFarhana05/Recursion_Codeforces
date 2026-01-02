import sys
sys.setrecursionlimit(10**7)

def s(i,arr):
    if i<0:
        return 0
    else:
        return arr[i]+s(i-1,arr)
n = int(input())
l = list(map(int,input().split()))
print(s(n-1,l))