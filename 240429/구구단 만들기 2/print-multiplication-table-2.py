a,b = map(int, input().split())

dans = [num for num in range(b,a-1,-1)]

for pwr in [2,4,6,8]:
    print(" / ".join([f"{dan} * {pwr} = {dan*pwr}" for dan in dans]))