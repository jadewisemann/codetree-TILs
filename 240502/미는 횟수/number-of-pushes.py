I = lambda: str(input())

s1, s2 = I(), I()
org = s1 * 2

print(len(s1) - org.index(s2))