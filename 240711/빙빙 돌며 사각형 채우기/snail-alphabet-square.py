MOVE = [ [0, 1], [1, 0], [0, -1], [-1, 0] ]

n, m = map(int,input().split())
grp = [[0]*m for _ in range(n)]

col_counter, low_counter = n-1, m
xx, yy = 0, -1
ord_a = ord("A") 
char = ord_a
move_idx = 0


while True:
    
    if low_counter == 0: break

    for _ in range(low_counter):

        dx, dy = MOVE[move_idx]
        xx += dx
        yy += dy

        grp[xx][yy] = chr(char)
        char = ord_a + (char - ord_a + 1)  % 26 

    low_counter -=  1

    move_idx = (move_idx + 1)  % 4

    
    if col_counter == 0: break

    for _ in range(col_counter):
        dx, dy = MOVE[move_idx]
        xx += dx
        yy += dy
        grp[xx][yy] = chr(char)

        char = ord_a + (char - ord_a + 1)  % 26 
        

    col_counter -= 1

    move_idx = (move_idx + 1)  % 4
    


for row in grp:
    for num in row:
        print(num, end=" ")
    print()