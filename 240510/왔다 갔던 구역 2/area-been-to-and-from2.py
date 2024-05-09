result = 0
arr = [0] * (2 * 100 * 10 + 1)
cur = 1000
min_cur = 2001
max_cur = 0

for _ in range(int(input())):

    max_cur = max(max_cur, cur)
    min_cur = min(min_cur, cur)

    val, direct = input().split()
    side = 1 if direct == "R" else -1
    
    for _ in range(int(val)):
        cur += side 
        arr[cur] += 1

counter = 0

for idx in range(min_cur, max_cur+1):
    if arr[idx] >= 2 : 
        counter += 1

print(counter)