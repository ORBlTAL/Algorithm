import sys
sys.stdin = open('input_3.text')
T = int(input())
for tc in range(1 , 1 + T):
    N , M = map(int , input().split())
    arr = [list(map(int , input().split())) for _ in range(N)]

    max_plus = 0 # 플러스 모양에서 최대합 저장 변수
    max_cross = 0 # 십자가 모양에서 최대합 저장 변수
    # 델타 방식 적용
    for r in range(N):
        for c in range(N):
            # 초기값은 지정한 곳의 값을 넣어줌
            sum_plus = arr[r][c] # 열을 넘어갈때 마다 스프레이 분사 범위내의 합을 구해야 하므로 여기서 합 구함
            for dr, dc in [[0,1],[1,0],[0,-1],[-1,0]]: # plus 모양으로 방향벡터 설정
                for i in range(1,M): # 0부터 시작하면 그 부분도 덧셈에 들어기나 1부터
                    nr , nc = r + (dr*i) , c + (dc*i) # 방향벡터에 1~M-1 의 i를 곱해줘서 전체 칸수 조회
                    if 0 <= nr < N and 0 <= nc < N: # 배열 범위 벗어나지 않도록 지정
                        sum_plus += arr[nr][nc] # 합을 구함
            if max_plus < sum_plus: # 최대값 갱신
                max_plus = sum_plus
    # 위와 동
    for r in range(N):
        for c in range(N):
            sum_cross = arr[r][c]
            for dr, dc in [[1,1],[1,-1],[-1,-1],[-1,1]]:
                for i in range(1,M):
                    nr , nc = r + (dr*i) , c + (dc*i)
                    if 0 <= nr < N and 0 <= nc < N:
                        sum_cross += arr[nr][nc]
            if max_cross < sum_cross:
                max_cross = sum_cross

    if max_plus > max_cross: # plus 모양으로 스프레이 분사한 결과가 더 크면
        print(f'#{tc}', max_plus) # plus 모양인 경우를 출력
    else:
        print(f'#{tc}', max_cross) # 아니면 십자가 모양인 경우를 출력