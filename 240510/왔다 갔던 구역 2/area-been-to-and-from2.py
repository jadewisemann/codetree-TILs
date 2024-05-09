vis = {}
cur = 0

for _ in range(int(input())):
    val, direct = input().split()
    for _ in range(int(val)):
        cur += (side:=1 if direct == "R" else -1)
        if cur in vis: 
            vis[cur] += 1
        else: 
            vis[cur] = 1

print(sum( 1 for value in vis.values() if value >= 2))