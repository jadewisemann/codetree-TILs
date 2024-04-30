size = int(input())
grp = [list(map(int,input().split())) for _ in range(size)]
rst_counter = 0

moves = [
    ( 1,  0), 
    ( 0,  1), 
    (-1,  0),
    ( 0, -1)
] 

dxs = [ 1, -1,  0,  0 ] 
dys = [ 0,  0,  1, -1 ]
 
for idx in range(size):
    for jdx in range(size):
        
        rst_counter += 1 if sum(
            0 <= idx + dx < size and 
            0 <= jdx + dy < size and 
            grp[idx + dx][jdx + dy] == 1
            for dx, dy in zip(dxs, dys)
        ) >= 3 else 0

print(rst_counter)