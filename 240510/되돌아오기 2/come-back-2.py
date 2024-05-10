CARDINALS = {
    "N" : (  0,  1 ), 
    "E" : (  1,  0 ), 
    "W" : ( -1,  0 ),
    "S" : (  0, -1 ), 
}

CLOCKWISE  = ["N", "E", "S", "W"]

# L => 왼쪽으로 90
# R => 오른쪽으로 90
# F => 전진

cur_point = "N"
X, Y = 0, 0
cnt = 0
flag = True
for char in str(input()):
    if char == "L":
        cur_point = CLOCKWISE[(CLOCKWISE.index(cur_point) + 4 - 1) % 4]
    elif char == "R":
        cur_point = CLOCKWISE[(CLOCKWISE.index(cur_point) + 4 + 1) % 4]
    elif char == "F":
        dx, dy = CARDINALS[cur_point]
        X += dx
        Y += dy

    cnt += 1

    if X == 0 and Y == 0:
        print(cnt)
        flag = False
        break

if flag: print(-1)