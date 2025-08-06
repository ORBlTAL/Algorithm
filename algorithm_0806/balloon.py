import sys
sys.stdin = open('input_4.text')
T = int(input())
for tc in range(1, 1 + T):
    N , M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 0 ,-1]
    dj = [1, 0, -1, 0]
    max_val = 0

    for r in range(N):
        for c in range(M):
            ball = arr[r][c]
            sum_val = arr[r][c]
            for k in range(4):
                for cnt in range(1, 1+ ball):
                    nr = r +di[k] * cnt
                    nc = c +dj[k] * cnt
                    if 0 <= nr < N and 0 <= nc < M:
                        sum_val += arr[nr][nc]

            if max_val < sum_val:
                max_val = sum_val
    print(f"#{tc} {max_val}")
    """
    헷갈린 부분 : for cnt in range(1, 1+ ball): 여기 범위. ball 이 1이어도 1번됨. 즉 상하좌우 1개씩만 터짐
    sum_val 에도 자기 자신을 넣어줘야함
    nr = r + di[k] 로 좌표를 이동해 주는데, 풍선안에 값이 2 이상이면 그만큼 가야하니
    cnt를 곱해서 그걸 구현
    for k in range 구문 내에서 반복하는 동안 arr[nr][nc]를 더해줘서 합을 구함
    초기화 되기전의 합과 max를 비교해 max에 넣기. max는 매 sum_val을 비교해서 최대값을 구함 
    """