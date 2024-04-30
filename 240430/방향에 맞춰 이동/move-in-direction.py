directions = {
    "N": [ 0,  1],
    "E": [ 1,  0],
    "S": [ 0, -1],
    "W": [-1,  0]
}

x_coor, y_coor = 0, 0
for _ in range(int(input())):
    direction, val  = input().split()
    dx, dy = directions[direction]
    x_coor += dx * int(val)
    y_coor += dy * int(val)
print(x_coor, y_coor)