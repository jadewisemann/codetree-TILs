n = int(input())
population = list(map(int, input().split()))
dist = [idx+1 for idx in range(n)]
rst = [] 

for place in range(n):
    temp_rst = 0
    dist_mod = []
    for d in dist:
        dist_mod.append(abs(d-(place+1)))

    for a,b in zip(population, dist_mod):
        temp_rst += a*b
    
    rst.append(temp_rst)


print(min(rst))