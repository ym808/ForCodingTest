n, m = map(int, input().split())
currencies = [int(input()) for _ in range(n)]

dp = [10001] * (m + 1)

dp[0] = 0

for cur in currencies:
    for i in range(cur, m + 1):
        dp[i] = min(dp[i], dp[i - cur] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])