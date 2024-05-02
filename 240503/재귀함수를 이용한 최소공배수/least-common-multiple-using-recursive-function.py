n = int(input())
nums = list(map(int, input().split()))

# euclidean algorithm w/recurrsion



def lcm_iter(numbers, idx = 0):

    def gcd(a,b):
        if b == 0:
            return a
        return gcd(b, a%b)

    def lcm(a,b):
        return (a*b) // gcd(a,b)

    if idx == n - 1:
        return (numbers[idx])
    
    return lcm(numbers[idx], lcm_iter(numbers, idx + 1))

print(lcm_iter(nums))