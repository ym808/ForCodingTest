import sys
N = int(input())
component_list = list(map(int, sys.stdin.readline().rstrip().split()))

M = int(input())
requirement_list = list(map(int, sys.stdin.readline().rstrip().split()))

max_int = max(component_list)
component_matrix = [0] * (max_int + 1)

for comp in component_list:
    component_matrix[comp] += 1

for req in requirement_list:
    if req > max_int:
        print("no")
    elif component_matrix[req] == 0:
        print("no")
    else:
        print("yes")

