ages = 0
num = 0
while True:
    try:
        age = int(input())
    except EOFError:
        break
        
    if ( age >= 30 ): break
    ages += age
    num += 1

print(f"{(ages/num):.2f}")