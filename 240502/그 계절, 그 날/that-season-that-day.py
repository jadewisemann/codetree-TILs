def sol(y,m,d): 

    def check_leap_years(year):
        return True if (
            (year % 4 == 0 and not year % 100 == 0) or
            year % 400 == 0
        ) else False
    
    # 1: 31 2: 28, 29 3: 31

    if not (
        m % 2 == 0 and d <= 30 or ( 
        m == 2 and ( 
            d <= 29 and (
            d == 29 and check_leap_years(y))
        ))
    ):
            return -1

    
    
    return (
        'Spring' if 3<= m <= 5  else
        'Summer' if 6<= m <= 8  else
        'Fall'   if 9<= m <= 11 else
        'Winter' 
    )


# Y, M, D = map(int, input().split())

print(sol(*list(map(int, input().split()))))