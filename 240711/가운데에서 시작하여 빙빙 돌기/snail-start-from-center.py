MOVE = [[0, -1], [-1, 0], [0, 1], [1, 0], ]

n= int(input())
grp = [[0]*n for _ in range(n)]

col_counter, low_counter = n, n-1
xx, yy = n-1, n
number  = n * n
move_idx = 0


while True:
    
    if col_counter == 0: break

    for _ in range(col_counter):
        dx, dy = MOVE[move_idx]
        xx += dx
        yy += dy
        grp[xx][yy] = number

        number -= 1

    col_counter -= 1

    move_idx = (move_idx + 1)  % 4
    
    if low_counter == 0: break

    for _ in range(low_counter):

        dx, dy = MOVE[move_idx]
        xx += dx
        yy += dy

        grp[xx][yy] = number
        number -= 1

    low_counter -=  1

    move_idx = (move_idx + 1)  % 4


for row in grp:
    for num in row:
        print(num, end=" ")
    print()