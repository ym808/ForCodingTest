T = 10
for test_case in range(1, T + 1):
    N = int(input())
    heights = list(map(int, input().split()))
    view_households = 0

    for i in range(2, N - 2):
        max_height = max(heights[i-2], heights[i-1], heights[i+1], heights[i+2])

        view_households += max(0, heights[i] - max_height)
    
    print(f"#{test_case} {view_households}")