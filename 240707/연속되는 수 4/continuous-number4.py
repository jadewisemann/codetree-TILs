def max_increasing_subsequence_length(n, sequence):
    if n == 0:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, n):
        if sequence[i] > sequence[i - 1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1

    return max_length

# 입력
n = int(input())
sequence = [int(input()) for _ in range(n)]

# 최대 길이 계산 및 출력
print(max_increasing_subsequence_length(n, sequence))