sums = 0

for _ in range(int(input())):
    sums += int(input())
sums = str(sums)

print(sums[1:] + sums[0])