n = int(input())
for i in range(1, (n*2 -1) +1):
    num_star = i if i<n else n*2 - i
    num_row = n + num_star
    print((" *"*num_star).rjust((num_row+1)," ")[2:])