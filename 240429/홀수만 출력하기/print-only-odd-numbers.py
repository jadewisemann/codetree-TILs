nums = [int(input()) for _ in range(int(input()))]

for num in nums:
    if (num%2 == 1) and (num % 3 == 0):
        print(num)