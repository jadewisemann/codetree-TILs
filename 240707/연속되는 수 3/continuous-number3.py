result = 0
last = 0
local= 1
for _ in range(int(input())):
    curr = int(input())
    if curr * last > 0 :
        local += 1
    else:
        result = max(local, result)
        local = 1

    last = curr
    
result = max(local, result)


print(result)