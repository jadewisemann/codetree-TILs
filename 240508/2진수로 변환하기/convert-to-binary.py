n = int(input())
rst=""
while n > 0:
    n, rest = divmod(n, 2)
    rst += str(rest) 
print(rst[::-1] if rst else 0)