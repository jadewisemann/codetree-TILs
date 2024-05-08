#             1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
MONTHS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

m1, d1, m2, d2 = map(int, input().split())

date_gap = sum(MONTHS[m1:m2]) - d1 + d2
index_gap = date_gap % 7 

print(DAYS[index_gap])