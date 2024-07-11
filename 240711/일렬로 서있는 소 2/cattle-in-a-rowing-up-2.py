n = int(input())
cows = list(map(int, input().split()))
l = len(cows)
rst = 0

for idx in range(l):
    for jdx in range(idx+1, l):
        for kdx in range(jdx+1, l):
            if cows[idx] <= cows[jdx] <= cows[kdx]:
                rst += 1

print(rst)