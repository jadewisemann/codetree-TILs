N = input()
rst = 0

for idx in range(len(N)):
    digit = N[idx]
 
    if digit == '0':
        rst = max(rst, int(  N[:idx] + '1' + N[idx+1:], 2))

rst = rst if rst  else int(N, 2)

print(rst)