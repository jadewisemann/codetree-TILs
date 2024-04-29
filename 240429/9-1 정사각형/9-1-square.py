n = int(input())
cnt = 0
curr = 9
for _ in range(n):
    for _ in range(n):
        if cnt > 8: cnt = 0
        print(curr-cnt, end ="")
        cnt += 1
    print()