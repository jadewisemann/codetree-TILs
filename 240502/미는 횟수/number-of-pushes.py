I = lambda: str(input())

s1, s2 = I(), I()
org = s1 * 2

if s2 in org:
    print(len(s1) - org.index(s2))
else:
    print(-1)