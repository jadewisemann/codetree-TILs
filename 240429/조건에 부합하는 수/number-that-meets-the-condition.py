for num in range(1, int(input()) + 1):
    if num % 2 == 0 and not num % 4 == 0: continue
    if (num // 8) % 2 == 0: continue
    if (num % 7) < 4: continue
    print(num, end=" ")