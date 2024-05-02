def print_recurr(number):
    
    if number == 0:
        return
    
    print("HelloWorld")

    return print_recurr(number-1)

print_recurr(int(input()))