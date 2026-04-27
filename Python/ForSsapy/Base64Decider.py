import string

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data = input()
    
    comp = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"
    decoded = []

    for d in data:
        i=0
        for c in comp:
            if d == c:
                decoded.append(i)
            i += 1
        
    i=0
    b = ""
    b_to_int = []

    for d in decoded:
        b += f"{d:06b}"
        i += 1
        if i >= 4: 
            for _ in range(3):
                b_to_int.append(int(b[:8], 2))
                b = b[8:]
            i=0
            b=""
            
    print(f"#{test_case}", end=" ")
    for i in b_to_int:
        print(chr(i), end="")
    print()
