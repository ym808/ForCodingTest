N = int(input())

students = []
for _ in range(N):
    name, score = input().split()
    students.append((name, int(score)))

students.sort(key=lambda x: x[1])
print(' '.join(name for name, _ in students))