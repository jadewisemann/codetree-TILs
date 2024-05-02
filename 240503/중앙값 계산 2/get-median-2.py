_ = int(input())
nums = list(map(int,input().split()))
rst = []

for idx, num in enumerate(nums):
    rst.append(num)
    rst.sort()
    if (idx+1)%2 == 1:
        print(rst[len(rst)//2], end=" ")