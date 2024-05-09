arr = [0] * 201
for _ in range(int(input())):
    a, b = map(int, input().split())
    for idx in range(a+100,b+100):
        arr[idx] += 1

print(max(arr))