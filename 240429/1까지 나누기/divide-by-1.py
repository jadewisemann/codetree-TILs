counter = 0
devider = 1
n = int(input())

while True:
    n //= devider
    devider += 1
    counter += 1
    if n < 1: break

print(counter)