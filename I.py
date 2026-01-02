def f(i,s):
    if i==len(s):
        return 0
    if s[i] in 'aeiouAEIOU':
        return f(i+1,s) + 1
    else:
        return f(i+1,s)
s = input()
print(f(0,s))