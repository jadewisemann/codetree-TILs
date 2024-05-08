ha, ma, hb, mb = map(int,input().split())
counter = 0
while True:
    
    if ha == hb and ma == mb:
        break
    
    if ma == 60:
        ha += 1
        ma = 0
        continue
    
    counter  += 1
    ma +=  1

print(counter)