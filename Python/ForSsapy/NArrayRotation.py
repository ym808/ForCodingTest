import copy
T = 1 #int(input())

for ts in range(1, T+1):
    N = int(input())
    grid = []
    rotated_grids = []
    for _ in range(N):
        row = input().split()
        grid.append(row)
    
    def turn(arr, N):
        result1 = ""
        result2 = ""
        result3 = ""
        for i in range(N):
            for j in range(N):
            # print(i, j)
                result1 += arr[N-j-1][i] # 90도
                result2 += arr[N-i-1][N-j-1] # 180도
                result3 += arr[j][N-i-1] # 180도
                print(result1, result2, result3)
                result1, result2, result3 = "", "", ""