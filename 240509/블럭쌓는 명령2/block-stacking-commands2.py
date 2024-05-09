I = lambda: map(int, input().split())
n, k = I()

arr = [0 for _ in range(n+1)]

for _ in range(k):
    a,b = I()
    for idx in range(a, b+1):
        arr[idx] += 1

print(max(arr))