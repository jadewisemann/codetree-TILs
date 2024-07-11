n = int(input())
rst = 0

for row in [ list(map(int, input().split())) for _ in range(n) ]:
    for idx in range(0,n-2):
        rst = max(rst, row[idx] + row[idx+1] + row[idx+2])
        
print(rst)