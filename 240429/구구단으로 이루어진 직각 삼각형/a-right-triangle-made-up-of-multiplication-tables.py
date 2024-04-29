n = int(input())
for num in range(1,n+1):
    print(" / ".join([f"{num} * {pwr} = {num*pwr}" for pwr in range(1,((n+1)- num)+1)]))