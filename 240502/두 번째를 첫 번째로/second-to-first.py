string = str(input())
first_char = string[0]
second_char = string[1]

rst_string = first_char
for char in string[1:]:
    if char == second_char:
        rst_string += first_char
    else:
        rst_string += char
print(rst_string)