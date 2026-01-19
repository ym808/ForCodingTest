N, K = map(int, input().split())
array_A = list(map(int, input().split()))
array_B = list(map(int, input().split()))

for _ in range(K):
    min_in_A = min(array_A)
    max_in_B = max(array_B)
    
    min_idx = array_A.index(min_in_A)
    max_idx = array_B.index(max_in_B)

    array_A[min_idx] = max_in_B
    array_B[max_idx] = min_in_A

print(sum(array_A))