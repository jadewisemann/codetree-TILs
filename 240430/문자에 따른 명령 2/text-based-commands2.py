"""

L : counter-clock
R : clockwise
F : move forward

init pos : north

"""

ORIENTS = {
    0: [ 0,  1],
    1: [ 1,  0],
    2: [ 0, -1],
    3: [-1,  0],
}

curr_orient = 0
curr_x, curr_y = 0, 0
for commend in str(input()):
    if commend == "L":
        curr_orient = (curr_orient - 1 + 4) % 4
    elif commend == "R":
        curr_orient = (curr_orient + 1 ) % 4
    elif commend == "F":
        dx,dy = ORIENTS[curr_orient]
        curr_x += dx
        curr_y += dy
print(curr_x, curr_y)