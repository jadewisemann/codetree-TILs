for _ in range(int(input())):
    a, b = map(int, input().split())
    rst = 0
    start = a + (0 if a%2 == 0 else 1)
    end = b + (1 if b%2 == 0 else 0) 
    for even in range(start, end, 2):
        rst += even
    print(rst)