import math

n = int(input())

ans = math.factorial(2 * n) // (
    math.factorial(n + 1) * math.factorial(n)
)

print(ans)