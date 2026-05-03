L = 7

items = [(1, 1),(3, 4),(4, 5),(5, 7)]

dp = [0] * (L+1)

for weight, value in items:
    for w in range(L, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + value)

print(dp[L])