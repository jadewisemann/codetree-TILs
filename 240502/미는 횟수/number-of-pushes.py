I = lambda: str(input())

s1, s2 = I(), I()

junctions = [idx for idx, char in enumerate(s2) if char == (first_char:=s1[0])] 

for juncion in junctions:
    if s1[juncion:] + s1[:juncion]  == s2:
        print(len(s1) - juncion)