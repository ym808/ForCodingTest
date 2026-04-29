base_table ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
chr_dict = {c:idx for idx, c in enumerate(base_table)}

T = int(input())
for t in range(T):
    encoded_str = input()
    
    decoded_str = []
    for c in encoded_str:
        decoded_str.append(chr_dict[c])
    
    raw_data = ""
    for i in range(0, len(decoded_str), 4):
        data = 0xFF & decoded_str[i]
        data = (data << 6) | decoded_str[i+1]
        data = (data << 6) | decoded_str[i+2]
        data = (data << 6) | decoded_str[i+3]

        raw_data += chr(0xFF & (data >> 16))
        raw_data += chr(0xFF & (data >> 8))
        raw_data += chr(0xFF & data)

    print(f"#{t} {raw_data}")
