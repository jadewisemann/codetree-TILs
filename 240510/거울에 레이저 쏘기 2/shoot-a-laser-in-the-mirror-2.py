"""
/ :
 위일때, 좌측, 아래일때, 우측

"""
CARDINALS = {  # clock wise
    "N" : ( -1,  0 ), 
    "E" : (  0,  1 ), 
    "W" : (  0, -1 ),
    "S" : (  1,  0 ), 
}

REFELECT = {
    "/" : {
        "N": "E",
        "E": "N",
        "W": "S",
        "S": "W",
    },
    "\\" : {
        "N": "W",
        "E": "S",
        "W": "N",
        "S": "E",
    }
}


n = int(input())
grp = [list(input()) for _ in range(n)]


X, Y, point = 0, 0, ""
start_pos = int(input())

if start_pos <= n:
    Y = start_pos -1
    point = "S"
elif start_pos <= n * 2:
    X = start_pos - n -1
    Y = n-1
    point = "W"
elif start_pos <= n * 3:
    X = n -1
    Y = 3*n - start_pos
    point = "N"
elif start_pos <= n * 4:
    X = 4*n - start_pos
    point = "E"

cnt = 0
while (0<= X < n and 0<= Y < n):
    point = REFELECT[grp[X][Y]][point]
    dx, dy = CARDINALS[point]
    X += dx 
    Y += dy
    cnt += 1
print(cnt)