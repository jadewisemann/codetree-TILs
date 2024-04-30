a, b = map(int, input().split())
rests = [0] * b


while True:
    if a  <= 1:    break
    rests[a % b] += 1
    a //= b


rst = 0     
for rest in rests:
    if rest == 0:   continue
    rst += rest**2
print(rst)