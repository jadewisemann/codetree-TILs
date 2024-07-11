string = str(input())
l = len(string)
rst = 0

for idx in range(l):
    if string[idx] == '(':
        for jdx in range(idx,l):
            if string[jdx] == ')':
                rst += 1
    
print(rst)