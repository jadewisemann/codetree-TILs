a, b = map(int, input().split()) 

# n[2] => n[10]
num = 0
for char in str(input()):
    num = num*a + int(char)

# n[10] => n[b]
result = ""
while num >= b:
    num, remainder = divmod(num, b)
    result += str(remainder)
result += str(num)
print(int(result[::-1]))