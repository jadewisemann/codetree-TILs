vis = {}
cur= 0
for _  in range(int(input())):

    val, direct = input().split()
    color = "B" if direct == "R" else "W"
    
    for _ in range(int(val)):
        if cur in vis:
            if len(vis[cur]) >= 3:
                vis[cur] += "G"
            else:
                vis[cur] += color
        else:
            vis[cur] = color
    
        cur += 1 if direct == "R" else -1
    
    cur += -1 if direct == "R" else 1

vals = [var[-1] for var in vis.values()]

print(vals.count("W"), vals.count("B"), vals.count("G"))