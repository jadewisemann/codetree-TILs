I = lambda : map(int, input().split())


COMFORT = [
    [  1,  0 ], 
    [ -1,  0 ], 
    [  0,  1 ], 
    [  0, -1 ]
]

n , m = I()

grp = [[False] * n for _ in range(n)] 

for _ in range(m):
    r, c = I()
    grp[r-1][c-1] = True
    cnt = 0
    for dx, dy in COMFORT:
        nx = r + dx -1
        ny = c + dy -1
        if not (0<= nx < n and 0<= ny < n): continue
        if grp[nx][ny]: cnt += 1
    print(1 if cnt >=3 else 0)