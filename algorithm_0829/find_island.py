# import sys
# sys.stdin = open('input.txt')
# N , M = map(int ,input().split())
# arr = [list(map(int, input())) for _ in range(N)]
# # print(arr)
# """
# 2개의 2차원 리스트를 동시에 탐색하는 방식은 어떨까?
# 동일하게 N*M 크기의 리스트를 만들어서 분석
# 하나는 받아온 그대로, 남은 하나는 모두 False 상태. 첫 조우시 1이면서 False 이면 델타를 통해서 1인 부분을 모두
# True로 바꿈. 순회 하면서 1이면서 False 부분만 해당 작업 실시.
# 1이면서 False를 조회한 수 자체를 세면 아마 답이 도출될 것.
# """
# dr = [0, 1, 1, 1, 0, -1, -1, -1]
# dc = [1, 1, 0, -1, -1, -1, 0, 1]
# state = [[False] * M for _ in range(N)]
#
# find_1_false_cnt = 0
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 1:
#             for k in range(8):
#                 ni, nj = i+dr[i] , j+dc[k]
#                 if 0<=ni<N and 0<=nj<M:
#                     if arr[ni][nj] == 1:
#                         state[ni][nj] = True
#             find_1_false_cnt +=1
# print(find_1_false_cnt)

import sys
sys.stdin = open('input.txt')
N , M = map(int ,input().split())
arr = [list(map(int, input())) for _ in range(N)]

# 섬을 찾기 위한 8방향 델타 선언
dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]
state = [[False] * M for _ in range(N)] # 2D 격자 크기와 동일한 Fasle 상태 배열

# dfs 함수 선언
def dfs(r,c):
    state[r][c] = True # 처음 입력 받은 좌표는 섬이므로 true로
    for k in range(8): # 델타 선언
        nr, nc = r + dr[k] , c + dc[k]
        if 0 <= nr < N and 0<= nc < M: # 범위 벗어나는거 방지
            if arr[nr][nc] == 1 and not state[nr][nc]: # 델타로 조회한 곳이 1이고 fasle 상태이면
                dfs(nr, nc) # 해당 좌표로 다시 델타 조회

find_1_false_cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and not state[i][j]: # 해당 좌표가1이고 상태가 false면
            find_1_false_cnt += 1 # 섬을 찾은 것이므로 +1 해주고
            dfs(i,j) # dfs 함수 호출
print(find_1_false_cnt)
#


