pos_A = [0]
pos_B = [0]
rst = 0
hall = []
N, M = tuple(map(int, input().split()))

for idx in range(N):
    v, t = tuple(map(int, input().split()))
    
    for _ in range(t):
        pos_A.append(pos_A[-1] + v)
        

for idx in range(M):
    v, t = tuple(map(int, input().split()))
    
    for _ in range(t):
        pos_B.append(pos_B[-1] + v)


for sec in range(max(len(pos_A), len(pos_B))):
    
    if sec == 0: continue
    
    if pos_A[sec] > pos_B[sec] and ['A'] != hall:
            rst += 1
            hall = ['A']
            
    if pos_A[sec] < pos_B[sec] and ['B'] != hall:
            rst += 1
            hall = ['B']
            
    if pos_A[sec] == pos_B[sec] and ['A', 'B'] != hall:
            rst += 1
            hall = ['A', 'B']
            
print(rst)