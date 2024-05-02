I = lambda: map(int, input().split())

n, m =  I()

global sequenc_A
sequenc_A = [0] + list(I())

for idx in range(1, n+1):
    sequenc_A[idx] += sequenc_A[idx-1]

for _ in range(m):
    a1, a2 = I()
    print(sequenc_A[a2] - sequenc_A[a1-1])