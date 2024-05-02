_ = int(input())
nums = list(map(int,input().split()))
rst = []

for num in nums:
    rst.append(num)
    rst.sort()
    if num%2 == 1:
        print(rst[len(rst)//2], end=" ")