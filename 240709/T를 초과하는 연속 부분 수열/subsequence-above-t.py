N, limit = map(int, input().split())
sequence = list(map(int, input().split()))


answer = 0
last_el = None
counter = 0

for el in sequence:
    if el > limit:
        if last_el is None or el > last_el:
            counter += 1
        else:
            answer = max(answer, counter)
            counter = 1
        last_el = el
    else:
        if counter > 0:
            answer = max(answer, counter)
        last_el = None
        counter = 0
        
answer = max(answer, counter)

print(answer)