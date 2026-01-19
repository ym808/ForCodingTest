N = int(input())

students = []
for _ in range(N):
    information = input().split()
    information[1] = int(information[1])
    students.append(information)

students.sort(key=lambda x: x[1])
for information in students:
    print(information[0], end=" ")
    