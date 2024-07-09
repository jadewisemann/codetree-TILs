N, K, P, T = tuple(map(int, input().split()))

status = [0] + [0 for _ in range(N)]
dureation = [0] + [0 for _ in range(N)]

status[P] = 1
dureation[P] = K

contact_info = [list(map(int, input().split())) for _ in range(T)]
contact_info.sort()

for _, a, b in contact_info:
    
    if dureation[a] and not status[b]:
        status[b] = 1
        dureation[b] = K
        dureation[a] -= 1
            

    if dureation[b] and not status[a]:
            status[a] = 1
            dureation[a] = K
            dureation[b] -= 1

print("".join(map(str, status[1:])))