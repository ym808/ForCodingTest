T = int(input())

for ts in range(1, T+1):
    def solve():
        sudoku = [list(map(int, input().split())) for _ in range(9)]
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                nums = []
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        nums.append(sudoku[r][c])
                if validate(nums) == False:
                    return False

        for i in range(9):
            if validate(sudoku[i]) == False:
                return False


        for c in range(9):
            nums = []
            for r in range(9):
                nums.append(sudoku[r][c])
            if validate(nums) == False:
                return False

        return True
    
    def validate(nums):
            nums = sorted(nums)
            for i in range(9):
                if nums[i] != i + 1:
                    return False
            return True

    result = 0
    if solve():
        result = 1
    

    print(f"#{ts} {result}")