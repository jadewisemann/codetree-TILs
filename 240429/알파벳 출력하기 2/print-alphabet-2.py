# ascii 65 = A, chr(65) = A
counter = 65
N = int(input())
for i in range(N):
    tmp = []
    for _ in range(N - i):
        tmp.append(chr(65+((counter-65))%26))
        counter += 1
    print(" ".join(tmp).rjust((N*2-1), " "))