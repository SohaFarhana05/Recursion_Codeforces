import sys
sys.setrecursionlimit(100000000)
def suffix(m,arr):
    if m==0:
        return 0
    else:
        return arr[-m]+suffix(m-1,arr)
n , m = map(int,input().split())
l = list(map(int,input().split()))
print(suffix(m,l))