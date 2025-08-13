import sys
sys.stdin = open('input_5.txt')
T = 10
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0 # 교착 상태의 개수를 세는 변수
    for j in range(N):
        state = 0 # 상태저장변수. 1을 조우할때만 1로 바뀜
        for i in range(N):
            if arr[i][j] == 1: # 순회하다가 1을 보면
                state = 1 # 상태를 1로 바꿈
            elif arr[i][j] == 2: # 2를 조우하게 되었을 때
                if state: # 상태가 1이라면, 즉 2를 조우하기 전에 이미 1을 만난 상황
                    cnt += 1 # 교착상태 이므로 +1
                    state = 0 # 이 이후부터는 다시 판단해야 하므로 state를 0으로 바꿔
                              # 다시 1을 조우하고 2를 만나는지 판단
    print(f'#{tc}',cnt)

"""
1 다음에 2가 나오는 경우만 세면 된다.
2가 여러개 라도 한번만 인식하면 된다.
1을 조우하지 않거나 1만 조우한 경우는 판단 안하게 하면 된다
상태판단 변수를 이용하면 될 듯? 
"""
