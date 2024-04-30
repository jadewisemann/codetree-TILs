I = lambda: map(int,input().split())
n, m = I()
grp1 = [[*I()] for _ in range(n)] 
grp2 = [[*I()] for _ in range(n)] 

for idx, row in enumerate(grp1):
    for jdx, el in enumerate(row):
        print(0 if grp2[idx][jdx] == el else 1, end=" ")
    print()