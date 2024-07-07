offset = 1000
factor = offset * 2 + 1
marker = 1

grp = [[0] * factor for _ in range(factor)] 

fxa, fya, fxb, fyb = list(map(lambda x: int(x) + offset, input().split()))
sxa, sya, sxb, syb = list(map(lambda x: int(x) + offset, input().split()))
minx, maxx, miny, maxy = factor, 0, factor, 0

for dx in range(sxa, sxb):
    for dy in range(sya, syb):
        grp[dx][dy] = marker

for dx in range(fxa, fxb):
    for dy in range(fya, fyb):
        if grp[dx][dy] != marker:
            minx = min(minx, dx)
            miny = min(miny, dy)
            maxx = max(maxx, dx)
            maxy = max(maxy, dy)


print(0 if (minx == factor or miny == factor or maxx == 0 or maxy == 0) else (maxx - minx + 1) * (maxy - miny + 1) )