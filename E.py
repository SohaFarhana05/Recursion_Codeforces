def b(i):
    if i==0:
        return ''
    return b(i//2) +str(i%2)
t = int(input())
for _ in range(t):
    n = int(input())
    if n==0:
        print(0)
    else:
        print(b(n))
