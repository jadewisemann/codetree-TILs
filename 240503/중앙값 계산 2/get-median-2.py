_ = int(input())
nums = list(map(int,input().split()))
rst = []

for num in nums:
    rst.append(num)
    if num%2 == 1:
        rst.sort()
        print(rst[len(rst)//2], end=" ")