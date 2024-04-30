rst = ""
for idx, el in enumerate(str(input())):  
    if (idx+1) % 2 == 0:
        rst += el
print(rst[::-1])