import sys
from itertools import permutations
sys.stdin = open('input_2.txt')
T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr= [list(map(int, input().split())) for _ in range(N)]
    a = list(range(N))
    min_val = float('inf')  # 최소값 선언
    for k in permutations(a): # N의 크기를 토대로 순열 생성하고, 각 요소를 k로 받음
        sum_val = 0 # 합 초기화
        for i in range(N):
            col_idx = k[i] # k의 i번째 요소들을 열 요소로 할당
            sum_val += arr[i][col_idx] # i는 행은 0,1,2, 순이고, 열은 순열에서 구한 순서로 인덱스 배치
        min_val = min(min_val,sum_val) # 최소 구하기
    print(f'#{tc}', min_val) # 출력

    # k = list(permutations(range(N))) # N의 크기를 토대로 arr의 위치를 지정할 수 있게 순열을 선언
    # min_val = float('inf') # 최소값 선언
    # for i in range(len(k)): # 모든 합의 경우에서
    #     sum_val = 0
    #     for j in range(N):
    #         sum_val += arr[j][k[i][j]] # 최소의 합을 찾아서 그걸 출력
    #     min_val = min(min_val, sum_val)
    # print(f'#{tc}', min_val)










# import sys
# sys.stdin = open('input_2.txt')
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     min_val = float('inf')
#     visited = [False] * N
#
#     def dfs(row, total):
#         global min_val
#         # 현재 합이 이미 최소보다 크면 가지치기
#         if total >= min_val:
#             return
#         # 모든 행을 다 배정했으면 최소값 갱신
#         if row == N:
#             min_val = min(min_val, total)
#             return
#         # 각 열 선택 시도
#         for col in range(N):
#             if not visited[col]:
#                 visited[col] = True
#                 dfs(row + 1, total + arr[row][col])
#                 visited[col] = False
#
#     dfs(0, 0)
#     print(f'#{tc}', min_val)
