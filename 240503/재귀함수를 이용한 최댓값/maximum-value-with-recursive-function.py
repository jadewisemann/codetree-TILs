def sol(nums, local_max = 0):
    if not nums:
        return local_max
    return sol(nums[1:], local_max:= max(local_max, nums[0]))
    
_ = int(input())

print(sol(list(map(int, input().split()))))