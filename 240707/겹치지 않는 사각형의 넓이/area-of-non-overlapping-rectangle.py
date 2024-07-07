offset = 1000
factor = offset * 2 + 1
min_x, max_x, min_y, max_y = factor, 0, factor, 0
result = 0
grp = [[0]* factor for _  in range(factor)]
for _ in range(2):
    x, y, xx, yy = list(map(lambda x: int(x) + offset, input().split()))
    for dx in range(x, xx) : 
        for dy in range(y, yy):
            if grp[dx][dy] == 0:
                grp[dx][dy] = 1
                result += 1

x, y, xx, yy = list(map(lambda x: int(x) + offset, input().split()))
for dx in range(x, xx) : 
    for dy in range(y, yy):
        if grp[dx][dy] == 1:
            result -= 1

print(result)