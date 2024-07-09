N, limit = map(int, input().split())
sequence = list(map(int, input().split()))


answer = 0
last_el = 0
counter = 0

for el in sequence:
    
    counter += 1
    
    if el <= limit or el <= last_el:
        answer = max(answer, counter-1)
        counter = 0
    
    last_el = el

print(answer)