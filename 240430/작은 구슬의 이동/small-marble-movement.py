ORIENTS = {
    "L" : ( -1,  0 ),
    "U" : (  0, -1 ),
    "D" : (  0,  1 ),
    "R" : (  1,  0 )
}

keys = list(ORIENTS.keys())



size, time = map(int, input().split())
curr_y, curr_x, direct = input().split()
curr_x = int(curr_x)
curr_y = int(curr_y)

while (time > 0):

    dx, dy = ORIENTS[direct]
    nx = curr_x + dx
    ny = curr_y + dy

    if (1<= nx <= size) and (1<= ny <= size):
        curr_x = nx
        curr_y = ny
    else:
        direct = keys[3 - keys.index(direct)]
    
    time -= 1
    
print(curr_y,curr_x)