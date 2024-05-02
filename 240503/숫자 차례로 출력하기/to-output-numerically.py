def sol(number, cnt = 1):

    if cnt > number :
        print()
        return

    print(cnt, end=" ")
    
    sol(number, cnt + 1)

    print(cnt, end=" ")

sol(int(input()))