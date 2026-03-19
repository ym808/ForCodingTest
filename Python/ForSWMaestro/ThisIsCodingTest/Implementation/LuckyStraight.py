n = input()

half = n // 2

front_str = n[:half]
back_str = n[half:]

front_sum = sum(map(int, front_str))
back_sum = sum(map(int, back_str))

if front_sum == back_sum:
    print("LUCKY")
else:
    print("READY")