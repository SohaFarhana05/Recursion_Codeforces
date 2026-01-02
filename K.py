def m(i,l,maxi):
    if i==0:
        return maxi
    if l[i]>maxi:
        maxi = l[i]
        return m(i-1,l,maxi)
    else:
        return m(i-1,l,maxi)

n = int(input())
l = list(map(int,input().split()))
print(m(n-1,l,l[0]))