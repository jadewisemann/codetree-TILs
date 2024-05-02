I = lambda: str(input())
str_org, str_sub = I(), I()

len_sub = len(str_sub)
cnt = 0

for i in range(len(str_org) - len_sub + 1):
    cnt += 1 if str_org[i:i+len_sub] == str_sub else 0
print(cnt)