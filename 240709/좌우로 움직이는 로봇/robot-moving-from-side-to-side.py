direction = {
    'L': -1,
    'R': 1
}

N, M = tuple(map(int, input().split()))
position_A, position_B = 0, 0
a_move, b_move = [], [] 
flag = True
rst = 0

for idx in range(N+M):
    
    reps, direct = tuple(input().split())
    
    if idx < N:
        a_move += [direction[direct]] * int(reps)
    else:
        b_move += [direction[direct]] * int(reps)

time_a = len(a_move)    
time_b = len(b_move)    
    
for sec in range(max(time_a, time_b)):
    if sec < time_a:
        position_A += a_move[sec]
    if sec < time_b: 
        position_B += b_move[sec]
    if position_A == position_B:
        if not flag:
            
            rst += 1
            flag = True
    else: 
        flag = False

print(rst)