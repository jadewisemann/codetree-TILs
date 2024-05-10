# tabulation

fibo =  [0,1,1]

N = int(input())

for _ in range(3, N+1):
    fibo.append(fibo[-1] + fibo[-2])

print(fibo[N])