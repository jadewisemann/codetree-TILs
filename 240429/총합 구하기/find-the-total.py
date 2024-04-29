answer = 0
a, b = map(int,input().split())

for num in range(a,b+1):
    answer += num if (num%6 == 0) and not (num%8 == 0) else 0

print(answer)