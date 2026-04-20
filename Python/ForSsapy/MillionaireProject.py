T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))
    
    max_price = 0
    sum_price = 0
    for i in range(len(prices)-1, -1, -1):
        if max_price < prices[i]:
            max_price = prices[i]
        else:
            sum_price += max_price - prices[i]

    print(f"#{test_case} {sum_price}")