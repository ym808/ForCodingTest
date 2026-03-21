s = input()

results = []

for i in range(1, len(s)+1):
    s_copy = s
    count = 1
    comp_str = ""
    while s_copy:
        prev = s_copy[:i]
        s_copy = s_copy[i:]

        if prev == s_copy[:i]:
            count += 1
        else:
            if count != 1:
                comp_str += str(count) + prev
                count = 1
            else:
                comp_str += prev
    results.append(comp_str)


print(min(map(len,results)))