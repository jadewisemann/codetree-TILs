N, T = tuple(map(int, input().split()))
command = str(input())

grp = []

for _ in range(N):
    grp.append(list(map(int, input().split())))

orient = [ [-1, 0], [0, 1], [1, 0], [0, -1] ]
orient_idx = 0

rst = 0

xx, yy = (N-1)//2, (N-1)//2

rst += grp[xx][yy]

for current_command in command:

    if current_command == 'L':
        orient_idx -= 1

    if current_command == 'R':
        orient_idx += 1

    if current_command == 'F':
        
        dx, dy = orient[orient_idx]
        nx = xx + dx
        ny = yy + dy
        
        if not ( 0<= nx < N and 0<= ny < N ):
            continue
        
        xx = nx 
        yy = ny

        rst += grp[xx][yy]

print(rst)