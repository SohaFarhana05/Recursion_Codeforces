def row(i,j,m,n):
    if j==len(m[0]):
        return []
    return [m[i][j]+n[i][j]] + row(i,j+1,m,n)
def addM(r,m,n):
    if r==len(m):
        return
    here = row(r,0,m,n)
    print(*here)
    addM(r+1,m,n)
r , c = map(int,input().split())
a = [ ]
b = [ ]
for i in range(r):
    t = list(map(int,input().split()))
    a.append(t)
for i in range(r):
    t = list(map(int,input().split()))
    b.append(t)
addM(0,a,b)