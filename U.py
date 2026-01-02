import sys
sys.setrecursionlimit(10**7)
def knapsack(i, w):
    if i == n or w == 0:
        return 0
    # Option 1: skip this item
    res = knapsack(i + 1, w)
    # Option 2: take this item (if possible)
    if wt[i] <= w:
        res = max(res, val[i] + knapsack(i + 1, w - wt[i]))
    return res
n, W = map(int, input().split())
wt = []
val = []
for _ in range(n):
    w, v = map(int, input().split())
    wt.append(w)
    val.append(v)
print(knapsack(0, W))