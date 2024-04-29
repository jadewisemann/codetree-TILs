N = int(input())
for idx in range(N):
    for num in range(N-idx, N+1):
        print(num, end=" ")
    print()