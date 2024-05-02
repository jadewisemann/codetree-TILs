_ = int(input())
nums = list(map(int,input().split()))
rst = []

for idx, num in enumerate(nums):
    rst.append(num)
    if (idx+1)%2 == 1:
        rst.sort()  
        print(rst[len(rst)//2], end=" ")