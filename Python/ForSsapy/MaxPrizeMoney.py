import sys

def solve():
    # 입력 데이터를 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    T = int(input_data[0])
    idx = 1
    
    for t in range(1, T + 1):
        num_str = input_data[idx]
        K = int(input_data[idx+1])
        idx += 2
        
        # 현재 교환 횟수에서 만들어질 수 있는 숫자들을 담는 Set (중복 제거용)
        current_states = {num_str}
        L = len(num_str)
        
        # K번 교환을 진행합니다.
        for _ in range(K):
            next_states = set()
            
            # 현재 만들어진 모든 숫자 상태에 대해 각각 다시 자리를 바꿉니다.
            for state in current_states:
                chars = list(state)
                
                # 중첩 반복문으로 바꿀 두 위치(i, j)의 모든 조합을 찾습니다.
                for i in range(L - 1):
                    for j in range(i + 1, L):
                        # i번째와 j번째 숫자를 교환 (Swap)
                        chars[i], chars[j] = chars[j], chars[i]
                        
                        # 교환한 결과를 다음 상태 Set에 추가
                        next_states.add("".join(chars))
                        
                        # 원상복구 (백트래킹): 다음 조합을 위해 원래대로 돌려놓음
                        chars[i], chars[j] = chars[j], chars[i]
            
            # 한 턴(1회 교환)이 끝났으므로, 상태를 갱신합니다.
            current_states = next_states
            
        # K번 교환이 모두 끝난 후, 모인 숫자들 중 가장 큰 값을 찾습니다.
        # 문자열은 길이가 같을 때 사전순으로 비교하므로 숫자의 대소 비교와 완벽히 일치합니다.
        ans = max(current_states)
        print(f"#{t} {ans}")

if __name__ == '__main__':
    solve()