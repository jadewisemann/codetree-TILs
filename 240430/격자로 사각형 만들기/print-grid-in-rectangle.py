size = int(input())

rst = [[1]*size]
for _ in range(size-1):
    curr_row = rst[-1]
    tmp_row = []
    val = 0
    for idx in range(size):
        val = 1 if idx == 0 else val + rst[-1][idx] + rst[-1][idx-1]
        tmp_row.append(val)
    rst.append(tmp_row)

for row in rst:
    for el in row:
        print(el, end=" ")
    print()