# a_n = a_{n-1} +  2 * a_{n-2}

num_arr = list(map(int, input().split()))

for i in range(10):
    if i >= 2:
        num_arr.append(num_arr[i-1] + num_arr[i-2]*2)
    print(num_arr[i], end=" ")