import sys
sys.stdin = open('input3.txt')
T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0]*N for _ in range(N)] # arr과 크기가 동일한 NxN 이고 내용은 전부 0

    dp[0][0] = arr[0][0] # 시작 위치의 값을 같게 해줌

    # 첫번째 행은 우측으로만 갈 수 있으므로
    for j in range(1, N):
        dp[0][j] = dp[0][j-1] + arr[0][j] # dp 좌표에 이전 arr 좌표와 현재 arr 좌표의 합을 더해 최소롤 구함

    # 첫번째 열은 아래쪽으로만 갈 수 있으므로
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + arr[i][0] # dp 좌표에 이전 arr 좌표와 현재 arr 좌표의 합을 더해 최소롤 구함

    # 위의 작업을 이후에서도 동일시 하는데, 최소를 비교해서 위와 우측 어디로 갈지를 정함
    for i in range(1,N):
        for j in range(1,N):
            dp[i][j] = arr[i][j] + min(dp[i-1][j], dp[i][j-1]) # dp 좌표는 현재 arr 좌표에서 이전 좌측, 이전 위측 에서 최소를 더함
    # 마지막 좌표에 여태까지의 누적합이 저장되므로 마지막 좌표를 출력
    print(f'#{tc}', dp[N-1][N-1])
