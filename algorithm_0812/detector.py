import sys
sys.stdin = open('input_0.txt')
T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt_0 = 0 # NxN 배열 전체에서의 0의 개수를 세는 변수
    cnt_1 = 0 # 경비병이 상하좌우로 조우했을때 기둥을 만나기 전까지 0의 개수를 세는 변수
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0: # 전체 배열에서의 0의 개수를 셈
                cnt_0 += 1
            if arr[i][j] == 2: # 경비병일 경우
                for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]: # 델타
                    for k in range(1, N-1): # 경비병 자신을 빼서 최대 N-1 크기 만큼 검사해야 하므로
                        ni , nj = i + di*k , j + dj*k
                        if not (0 <= ni < N and 0 <= nj < N): # 범위를 벗어나면 break.
                            break
                        if arr[ni][nj] == 1: # 기둥 조회시 break
                            break
                        if arr[ni][nj] == 0: # 0이면 개수를 센다
                            cnt_1 += 1

    print(f"#{tc}", cnt_0-cnt_1) # NxN 전체 0의 개수에서 경비병이 탐색한 0의 개수를 빼면 눈을 피할 수 있는 공간임