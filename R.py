import sys
sys.setrecursionlimit(10**7)

def palindrome(i,arr):
    if i>=len(arr)//2:
        return True
    if arr[i]==arr[len(arr)-i-1]:
        return palindrome(i+1,arr)
    return False
n = int(input())
l = list(map(int,input().split()))
if palindrome(0,l):
    print("YES")
else:
    print("NO")
    