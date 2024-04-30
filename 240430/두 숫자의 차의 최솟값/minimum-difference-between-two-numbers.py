_ = int(input())
numbers = list(map(int, input().split()))
results = []
pre_num = 0
for num in numbers:
    if pre_num:
        results.append(num-pre_num)
    pre_num = num 
print(min(results))