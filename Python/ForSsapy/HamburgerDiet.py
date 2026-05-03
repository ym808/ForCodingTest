import itertools

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    
    ingredients = []
    dp = [0] * (L + 1)

    for i in range(N):
        score, calory = map(int, input().split())
        ingredients.append((score, calory))

    for score, calory in ingredients:
        for c in range(L, calory - 1, -1):
            dp[c] = max(dp[c], dp[ - calory] + score)
    
    print(f"#{test_case} {dp[L]}")
