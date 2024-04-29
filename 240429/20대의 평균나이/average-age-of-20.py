ages = 0
num = 0
while True:
    age = int(input())        
    if not( (20 <= age) and (age< 30) ): break
    ages += age
    num += 1

print(f"{(ages/num):.2f}")