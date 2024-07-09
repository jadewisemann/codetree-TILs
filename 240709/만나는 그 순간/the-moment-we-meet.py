direction = {
    'L' : -1, 
    'R' : 1
}

N, M = tuple(map(int, input().split()))

pos_A, pos_B = 0, 0
rst = -1

a_moves, b_moves = [], []

for idx in range(N+M):

    direct, value = tuple(input().split())

    if idx < N:
        a_moves += [direction[direct]]*int(value)
    else:
        b_moves += [direction[direct]]*int(value)
        
for tick in range(len(a_moves)):
    
    pos_A += a_moves[tick]
    pos_B += b_moves[tick]
    
    if pos_A == pos_B:
        rst = tick + 1
        break

print(rst)