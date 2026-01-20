N = int(input())
components = set(map(int, input().split()))

M = int(input())
requirements = list(map(int, input().split()))

for req in requirements:
    if req in components:
        print("yes")
    else:
        print("no")