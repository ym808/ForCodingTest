import sys

input = sys.stdin.readline

# max 매번 찾기 vs max 한개 찾아두고 바뀔 때만 찾기

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))

    rep = len(prices)
    profit_sum = 0

    for i in range(rep):
        max_price = prices[i]

        for j in range(i + 1, rep):
            if max_price < prices[j]:
                max_price = prices[j]

        if max_price == prices[i]: continue
        profit_sum += max_price - prices[i]

    print(f"#{test_case} {profit_sum}")

                