result = 0
offset = 100
factor = offset * 2 + 1
grp = [[0] * factor  for _ in range(factor)]
for _ in range(int(input())):
    a,aa, b, bb = list(map(lambda x: int(x) + offset, input().split()))
    for x_cord in range(a, b):
        for y_cord in range(aa, bb):
            if grp[x_cord][y_cord] == 0 :
                grp[x_cord][y_cord] = 1
                result += 1
print(result)