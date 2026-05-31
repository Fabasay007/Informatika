n, m = map(int, input().split())
field = []
for _ in range(n):
    field.append(list(map(int, input().strip())))
dp = [-1] * m
for i in range(n - 1, -1, -1):
    for j in range(m):
        if i == n - 1 and j == 0:
            dp[j] = field[i][j]
            continue
        best = -1
        if i + 1 < n:
            best = max(best, dp[j])
        if j - 1 >= 0:
            best = max(best, dp[j - 1])
        dp[j] = best + field[i][j]
print(dp[m - 1])