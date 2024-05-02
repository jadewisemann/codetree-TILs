def solution(n1, n2):
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    return (n1 * n2) // gcd(n1, n2)

n1, n2 = map(int, input().split())
print(solution(n1,n2))