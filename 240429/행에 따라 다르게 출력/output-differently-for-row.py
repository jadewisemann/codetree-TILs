n = int(input())
curr = 0
for i in range(1,n+1):
    add_val = 1 if i%2 == 1 else 2
    for _ in range(n):
        curr += add_val 
        print(curr, end=" ")
    print()