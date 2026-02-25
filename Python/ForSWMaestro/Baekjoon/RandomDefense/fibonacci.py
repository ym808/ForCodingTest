t = int(input())

max_n = 40

n_0 = [0] * (max_n + 1)
n_1 = [0] * (max_n + 1)

n_0[0], n_1[0] = 1, 0
n_0[1], n_1[1] = 0, 1

for i in range(2, max_n + 1):
    n_0[i] = n_0[i-1] + n_0[i-2]
    n_1[i] = n_1[i-1] + n_1[i-2]

n = [int(input()) for _ in range(t)]

for i in n:
    print(n_0[i], end=" ")
    print(n_1[i])
