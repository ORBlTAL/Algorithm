
"""
행 순회 하면서 1을 만나면 cnt +=1 해줘서 세줌. 0을 조우하면 다시 리셋하고 그 다음 1부터 다시 세도록
만약 마지막이 0으로 안끝날시 여태 센 cnt가 M과 동일하면 그때도 경우를 세줌.
cnt == M 인 경우를 세줘서 넣을 수 있는 단어의 개수를 세주면 될 거 같음.
"""
import sys
sys.stdin = open('input_4.txt')
T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    output = 0 # 넣을 수 있는 단어의 개수를 세는 변수
    # 가로행 탐색
    for i in range(N):
        cnt = 0 # 1의 개수를 세주는 변수 cnt
        for j in range(N):
            if arr[i][j] == 1: # 1과 조우시마다 cnt를 세줌
                cnt += 1
            else: # arr[i][j]가 0이면
                if cnt == M: # 그 이전까지 센 cnt가 1이면 output 에 +1
                    output += 1
                cnt = 0 # cnt 초기화
        if cnt == M: # 마지막이 1로 끝날시에는 위 else문이 작동 안하므로 여기서 판별. cnt가 M이면 output에 +1
            output += 1
    # 세로행 탐색
    for j in range(N): # 위와 동일
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == M:
                    output += 1
                cnt = 0
        if cnt == M:
            output += 1

    print(f'#{tc}',output)
