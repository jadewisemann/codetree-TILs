counter = 0
for num in [int(input()) for _ in range(5)]:
    if num % 2 == 0:
        counter += 1
print(counter)