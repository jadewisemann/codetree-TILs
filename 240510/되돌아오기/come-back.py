CARDINALS = {
    "N" : (  0,  1 ), 
    "E" : (  1,  0 ), 
    "W" : (  -1, 0 ),
    "S" : ( 0,  -1 ), 
}

def sol():
    X, Y = 0, 0 
    cnt = 0
    for _ in range(int(input())):    
        point, value = input().split()
        dx, dy = CARDINALS[point]
        for _ in range(int(value)):
            X += dx
            Y += dy
            cnt += 1 
            if X == 0 and Y == 0:
                return cnt                
    return -1

print(sol())