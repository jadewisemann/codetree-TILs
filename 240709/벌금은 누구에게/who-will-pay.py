N, M, K = tuple(map(int, input().split()))

students = [idx +  1 for idx in range(N)]
penalties = [K for _ in range(N)]
rst = -1

for _ in range(M):
    num = int(input())
    
    if penalties[ num - 1 ] == 1:
        rst = num
        break

    penalties[num - 1] -= 1

print(rst)