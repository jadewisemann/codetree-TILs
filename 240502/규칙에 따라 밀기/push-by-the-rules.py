I = lambda: str(input())

org = I()

for commend in I():
    if commend == "R": 
        org = org[-1] + org[:-1] 
    elif commend == "L":
        org = org[1:] + org[0]
        
print(org)