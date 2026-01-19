array = [('개', 1), ('원숭이',-1), ('고양이',2)]

def setting(data):
    return data[1]

new_arr = sorted(array, key=lambda x : x[1])
print(max(new_arr, key=lambda x:x[1]))
print(new_arr)