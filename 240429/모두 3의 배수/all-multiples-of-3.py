ans = 1
for _ in range(5):
    if ans: continue
    if not int(input()) % 3 == 0:
        ans = 0
print(ans)