size = int(input())
grp = [[0] * size for _ in range(size)]

curr = 0

for idx in range(size-1, -1, -1):  # 3,2,1,0
    for jdx in range(size):  # 0,1,2,3
        if idx%2 == 1:
            jdx = size -1 - jdx
        curr += 1
        grp[jdx][idx] = curr

for row in grp:
    for el in row:
        print(el, end=" ")
    print()