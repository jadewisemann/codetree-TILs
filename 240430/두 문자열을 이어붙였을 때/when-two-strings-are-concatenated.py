I = lambda: str(input())
str_a, str_b = I(), I()

print('true' if str_a + str_b == str_b + str_a else 'false')