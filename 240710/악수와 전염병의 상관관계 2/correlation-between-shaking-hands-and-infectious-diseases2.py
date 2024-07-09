N, K, P, T = tuple(map(int, input().split()))

devs = [0] + [idx + 1 for idx in range(N)]
status = [0] + [0 for _ in range(N)]
dureation = [0] + [0 for _ in range(N)]
status[P] = 1
dureation[P] = K

contact_info = sorted(
    [list(map(int, input().split())) for _ in range(T)]
)

for _, a, b in contact_info:

    if dureation[a]:    
        if not status[b]:
            status[b] = 1
            dureation[b] = K
        dureation[a] -= 1
            

    if dureation[b]:
        if not status[a]:
            status[a] = 1
            dureation[a] = K
        dureation[b] -= 1

print("".join(map(str, status[1:])))