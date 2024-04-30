I = lambda: map(int, input().split())
n, m = I()
grp = [[0]*n for _ in range(n)]
for _ in range(m):
    xx, yy = I()
    grp[xx-1][yy-1] = xx*yy

for row in grp:
    for el in row:
        print(el, end=" ")
    print()