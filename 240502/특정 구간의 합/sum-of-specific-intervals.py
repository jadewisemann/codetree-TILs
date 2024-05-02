I = lambda: map(int, input().split())


n, m =  I()

global memo_sums
memo_sums = [0] * (n+1)

def partial_sum (a,b):
    if not memo_sums[b]:
        for idx in range(1, b+1):
            if not memo_sums[idx]:
                memo_sums[idx] = memo_sums[idx-1] + sequenc_A[idx]
    return(memo_sums[b] - memo_sums[a-1] )



global sequenc_A
sequenc_A = [0] + list(I())

for _ in range(m):
    a1, a2 = I()
    print(partial_sum(a1, a2))