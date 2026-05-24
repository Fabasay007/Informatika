n, m = map(int, input().split())

field = []
for _ in range(n):
    field.append(list(map(int, input().strip())))

dp = [[0] * m for _ in range(n)]
dp[n - 1][0] = field[n - 1][0]

for i in range(n - 1, -1, -1):
    for j in range(m):

        if i == n - 1 and j == 0:
            continue
        best = -1

        if i + 1 < n:
            best = max(best, dp[i + 1][j])

        if j - 1 >= 0:
            best = max(best, dp[i][j - 1])

        dp[i][j] = best + field[i][j]
print(dp[0][m - 1])