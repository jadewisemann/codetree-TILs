arr = [0] * (100 + 1)
for _ in range(int(input())):
    a, b = map(int, input().split())
    for idx in range(a,b+1):
        arr[idx] += 1
print(max(arr))