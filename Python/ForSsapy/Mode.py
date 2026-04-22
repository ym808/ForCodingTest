T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    scores = list(map(int, input().split()))

    frequency = [0] * 101

    for score in scores:
        frequency[score] += 1

    max_f = 0
    for i in range(101):
        if frequency[i] >= max_f:
            max_f = frequency[i]
            where_max_f = i            

    print(f"#{test_case} {where_max_f}")