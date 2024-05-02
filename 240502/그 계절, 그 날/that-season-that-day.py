def sol(y,m,d): 

    def check_leap_years(year):
        return True if (
            (year % 4 == 0 and not year % 100 == 0) or
            year % 400 == 0
        ) else False

    if d == 29 and not check_leap_years(y):
            return -1
    
    return (
        'Spring' if 3<= m <= 5  else
        'Summer' if 6<= m <= 8  else
        'Fall'   if 9<= m <= 11 else
        'Winter' if m <= 2 or m == 12 else
        -1
    )


# Y, M, D = map(int, input().split())

print(sol(*list(map(int, input().split()))))