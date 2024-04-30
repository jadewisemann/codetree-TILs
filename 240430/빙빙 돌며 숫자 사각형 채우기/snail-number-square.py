ORIENTS = {
    0 : (  0,  1 ), 
    1 : (  1,  0 ), 
    2 : (  0, -1 ),
    3 : ( -1,  0 ), 
}

n, m = map(int,input().split())
grp = [[0]*m for _ in range(n)]

xx, yy, direct, curr_num = 0, -1, 0, 1

while (curr_num <= n*m):
    dx, dy = ORIENTS[direct]
    nx, ny = xx + dx, yy + dy

    if not (
        0<= ny < m and
        0<= nx < n and
        grp[nx][ny] == 0 
    ) :
        direct = (direct + 1) % 4
        continue
    
    xx, yy = nx, ny
    
    grp[xx][yy] = curr_num
    curr_num += 1

for row in grp:
    for el in row:
        print(el, end=" ")
    print()