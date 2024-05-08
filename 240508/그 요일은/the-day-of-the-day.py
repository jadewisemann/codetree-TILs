#             1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
MONTHS = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

m1, d1, m2, d2 = map(int, input().split())
target_date = str(input())


total_date = lambda m,d : sum(MONTHS[:m]) + d

date_gap = abs(total_date(m1,d1) - total_date(m2,d2))

print(date_gap//7 + (1 if date_gap%7 >= DAYS.index(target_date) else 0))