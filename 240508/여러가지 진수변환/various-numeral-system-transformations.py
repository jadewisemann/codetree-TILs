N, B = map(int, input().split())
result = ""
while N >= B:
    N, res = divmod(N,B)
    result += str(res)
result += str(N)
print(result[::-1])