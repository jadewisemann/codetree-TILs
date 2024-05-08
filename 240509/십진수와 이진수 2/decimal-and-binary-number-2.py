n = 0
for char in str(input()):
    n = n*2 + int(char)
n *= 17

result = ""
while n >= 2:
    n, remainder = divmod(n,2)
    result += str(remainder)
result += str(n)

print(int(result[::-1]))