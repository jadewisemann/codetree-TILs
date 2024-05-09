OFFSET = 1000 * 100
WHITE, BLACK = 111, 333 
arr = [0] * (OFFSET * 2 + 1)  
cur = 0

for _ in range(int(input())):
    
    val, dirt = input().split()
    val = int(val)
    if dirt =="L" :
        for idx in range(val):
            arr[cur - idx + OFFSET] = WHITE
        cur -= val - 1

    elif dirt == "R":
        for idx in range(val):
            arr[cur + idx + OFFSET] = BLACK
        cur += val - 1

flt_arr = list(filter(lambda x: x != 0, arr))
print(flt_arr.count(WHITE),flt_arr.count(BLACK))