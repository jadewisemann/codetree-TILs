N, M = tuple(map(int, input().split()))
position_A, position_B = 0, 0
a_velocity, b_velocity = [], []
leader, last_leader = None, None
rst = 0

for idx in range(N+M):
    
    v, t = tuple(map(int, input().split()))
    
    if idx < N:
        a_velocity += [v]*t
    else:
        b_velocity += [v]*t
        
for sec in range(len(a_velocity)):
    
    position_A += a_velocity[sec]
    position_B += b_velocity[sec]
    
    if position_A > position_B: 
        leader = 'A'
    elif position_B > position_A: 
        leader = 'B'
    
    if leader != None and last_leader!=None and leader != last_leader:
        rst += 1
    
    last_leader = leader

print(rst)