dp = [0] * (N:= int(input()))
arr = list(map(int,input().split()))

for idx in range(1, N):
    dp[idx] = max(([dp[jdx] for jdx in filter(lambda jdx: arr[jdx] <= arr[idx] ,[jdx for jdx in range(idx)])])) + 1
print (max(dp)+1)