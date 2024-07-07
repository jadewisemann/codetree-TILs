# result = 0
# last = 0
# local= 1
# for _ in range(int(input())):
#     curr = int(input())
#     if curr == last :
#         local += 1
#     else:
#         result = max(local, result)
#         local = 1

#     last = curr

# print(result)

result = 0
last = None
local = 0

for _ in range(int(input())):
    curr = int(input())
    if curr == last:
        local += 1
    else:
        result = max(local, result)
        local = 1  # 새로 시작할 때 1로 시작해야 합니다.
    
    last = curr

result = max(local, result)  # 마지막 연속된 숫자의 길이를 반영

print(result)