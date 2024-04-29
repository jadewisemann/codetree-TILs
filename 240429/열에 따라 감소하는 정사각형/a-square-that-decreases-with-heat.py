n = int(input())

for _ in range(n):
    print(' '.join(map(str, [i for i in range(n,0,-1)])))