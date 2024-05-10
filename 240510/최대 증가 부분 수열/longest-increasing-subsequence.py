dp = [1] * (N:= int(input()))
arr = list(map(int,input().split()))

for idx in range(1, N):
    dp[idx] = max([dp[jdx] for jdx in range(idx) if arr[jdx] <= arr[idx]], default=0) + 1
print (max(dp))