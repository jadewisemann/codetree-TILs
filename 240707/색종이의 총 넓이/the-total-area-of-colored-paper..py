offset = 100
factor = offset * 2 + 1

side = 8

grp = [[0] * factor for _ in range (factor)]

result = 0

for _ in range(int (input())):
    x, y = list(map(lambda x: int(x) + offset, input().split()))
    for dx in range(x, x+8):
        for dy in range(y, y+8):
            if grp[dx][dy] == 0:
                grp[dx][dy] = 1
                result += 1
print(result)