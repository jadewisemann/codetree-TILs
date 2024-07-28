R, C = tuple(map(int, input().split()))
grp = [list(map(str, list(input().split()))) for _ in range( R )]

starting, stopovers, counter  = grp[0][0], [ ], 0

for idx in range( R-1 ):
    for jdx in range( C-1 ):
        if grp[idx][jdx] != starting:
            stopovers.append([idx, jdx])


for xx, yy in stopovers:
    for idx in range(xx+1, R-1):
        for jdx in range(yy+1, C-1):
            if grp[idx][jdx] == starting:
                counter += 1
                
print(counter)