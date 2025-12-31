def f(i,arr):
    if i<0:
        return ''
    elif i==0:
        return str(arr[0])
    elif i%2==0:
        return str(arr[i]) + ' ' + f(i-2,arr) 
    else:
        return f(i-1,arr)
n = int(input())
l = list(map(int,input().split()))
print(f(n-1,l))