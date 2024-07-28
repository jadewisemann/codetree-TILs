def sol():
    R, C = map(int, input().split())
    grid = [input().split() for _ in range(R)]
    
    def count_paths(x1, y1, x2, y2):
        if grid[x1][y1] == grid[x2][y2]:
            return 0
        return 1
    
    total = 0
    for i in range(1, R-1):
        for j in range(1, C-1):
            for k in range(i+1, R-1):
                for l in range(j+1, C-1):
                    total += count_paths(0, 0, i, j) * count_paths(i, j, k, l) * count_paths(k, l, R-1, C-1)
    
    return total

print(sol())