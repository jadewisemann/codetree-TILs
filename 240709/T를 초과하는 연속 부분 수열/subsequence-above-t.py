N, limit = map(int, input().split())
sequence = list(map(int, input().split()))

answer = 0
counter = 0

for i in range(N):
    if sequence[i] > limit:
        if i == 0 or sequence[i] > sequence[i - 1]:
            counter += 1
        else:
            counter = 1
        answer = max(answer, counter)
    else:
        counter = 0

print(answer)