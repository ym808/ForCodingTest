

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    heights = list(map(int, input().split()))
    view_households = 0

    for i in range(2, len(heights)-2):
        gaps = []
        gaps.append(heights[i] - heights[i - 2])
        gaps.append(heights[i] - heights[i - 1])
        gaps.append(heights[i] - heights[i + 1])
        gaps.append(heights[i] - heights[i + 2])
        
        # 4범위 안의 건물 높이가 같거나 높은 경우
        no_gap = False
        for gap in gaps:
            if gap <= 0:
                no_gap = True
        
        if no_gap: continue
        # 4범위 안의 건물 높이가 작은 경우
        min_gap = min(gaps)
        view_households += min_gap

    print(f"#{test_case} {view_households}")
        