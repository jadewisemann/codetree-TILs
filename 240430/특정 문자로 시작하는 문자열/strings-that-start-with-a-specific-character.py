counter = 0
len_sum = 0

strings = [str(input()) for _ in range(int(input()))]
target_char= str(input())

for string in strings:
    if string.startswith(target_char):
        counter += 1
        len_sum += len(string)
print(f"{counter} {(len_sum/counter):.2f}")