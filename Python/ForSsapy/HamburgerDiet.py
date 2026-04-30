import itertools

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    preference = []
    scores = []

    for _ in range(N):
        score, cal = map(int, input().split())
        preference.append((score, cal))

    # 모든 조합을 다 시도하고 제한 칼로리 미만 조합 중 가장 점수 높은 거

    for i in range(1, 21):
        combos = list(itertools.combinations(preference, i))

        for combo in combos:
            total_score = 0
            total_calory = 0
            for j in range(len(combo)):
                total_score += combo[j][0]
                total_calory += combo[j][1]
            if total_calory <= L: scores.append(total_score)

    print(f"#{test_case} {max(scores)}")
    

    