# """
#    0인곳만 이동할 수 있으며, 3을 찾으면 1을 출력, 아니면 0
#    갔다가 다시 돌아와야함
#    일단 시작 지점을 2로 잡고 거기를 True로 변경. 0 이면서 False인 곳만 갈 수 있고, 3 조회시 멈춤
# """
import sys
sys.stdin = open('input_1.txt')
T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int ,input())) for _ in range(N)]

    dr = [0, 1, 0, -1] # 상하좌우 델타 선언
    dc = [1, 0, -1 ,0]

    state = [[False] * N for _ in range(N)]
    found = [0] # 3을 찾았을 때 답을 넣을 1x1 리스트

    def dfs(r,c):
        if arr[r][c] == 3: # 3을 찾으면
            found[0] = 1 # 1을 할당
            return

        state[r][c] = True # 입력 받은 좌표 상태를 true로

        for k in range(4): # 상하좌우 델타 활용
            nr , nc = r + dr[k] , c + dc[k]
            if 0 <= nr < N and 0 <= nc < N: # 인덱스 범위 벗어나는거 방지
                if (arr[nr][nc] == 0 or arr[nr][nc] ==3) and not state[nr][nc]: # 조회한 좌표가 0또는 3이면서, 상태가 False일 때
                    dfs(nr,nc) # 해당 좌표로 다시 델타 계산
    x = y = -1 # 2의 좌표 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x = i
                y = j
                break # 찾으면 break
        if x != -1: # 바깥 for문도 break
            break
    dfs(x,y) #dfs로 풀기
    print(f'#{tc}',found[0])


