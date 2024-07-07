BLANK = 0
BLUE = 1
RED = 2

curr_color = {
    0: BLUE,
    1: RED
}

offset = 100
factor = offset * 2  + 1

grp = [[BLANK] * factor for  _ in range(factor)]
result = 0

for idx in range(int(input())):
    color = idx % 2  # 0 for blue, 1 for red
    sx, sy, ax, ay = map(lambda x: int(x) + offset, input().split())

    if color == 1: # blue 
        for dx in range(sx, ax):
            for dy in range(sy, ay):
                if grp[dx][dy] != BLUE:
                    grp[dx][dy] = BLUE
                    result += 1
    else: # red
        for dx in range(sx, ax):
            for dy in range(sy, ay):
                grp[dx][dy] = RED
                if grp[dx][dy] == BLUE:
                    result -= 1        

print(result)