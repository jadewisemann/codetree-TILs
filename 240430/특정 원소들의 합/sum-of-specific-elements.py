SIZE = 4
rst = 0
for idx in range(SIZE) :
    rst += sum(list(map(int,input().split()))[:(idx+1)])
print(rst)