ans = 0
for _ in range(5):
    if ans: continue
    if int(input()) % 3 == 0:
        ans = 1
print(ans)