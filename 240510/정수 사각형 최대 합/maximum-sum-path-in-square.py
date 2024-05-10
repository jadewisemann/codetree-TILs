N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

memo = [[0]* N for idx in range(N)]

memo[0][0] = grid[0][0]
for idx in range(1,N):
    memo[idx][0] = grid[idx][0] + memo[idx-1][0]
    memo[0][idx] = grid[0][idx] + memo[0][idx-1]

for idx, row in enumerate(memo):
    for jdx,el in enumerate(row):
        if el != 0: continue
        memo[idx][jdx] = grid[idx][jdx] + max(memo[idx][jdx-1], memo[idx-1][jdx])
print(max(memo[-1]))