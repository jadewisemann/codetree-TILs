def sol(n, cur = 1):
    if cur > n:
        return
    print("*" * cur)
    sol(n, cur+ 1)

sol(int(input()))