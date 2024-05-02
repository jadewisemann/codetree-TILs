flag = False
rst = ""
for char in str(input()):
    if char == 'e' and not flag :
        flag = True
        continue
    rst += char
print(rst)