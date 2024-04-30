size = int(input())
grp = [list(map(int,input().split())) for _ in range(size)]
rst_counter = 0

moves = [
    [ 1,  0], 
    [ 0,  1], 
    [-1,  0],
    [ 0, -1]
] 

for idx in range(size):
    for jdx in range(size):
        tmp_counter = 0
        for dx, dy in moves:
            nx = idx + dx
            ny = jdx + dy
            
            if (nx >= size or nx < 0 ) or (ny >= size or ny < 0):
                continue

            if grp[nx][ny] == 1:
                tmp_counter += 1 

            if tmp_counter >= 3:
                rst_counter += 1
                break

print(rst_counter)