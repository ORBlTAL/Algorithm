# import sys
# sys.stdin = open('input_05.text')
# T = int(input())
#
# for tc in range(1, T + 1):
#     arr = [list(map(int, input().split())) for _ in range(100)]
#     answer = 0
#     for i in range(100):
#         if arr[99][i] == 2:
#             answer = i
#             break
#
#     start_point = arr[99][answer]
#     for r in range(99,-1,-1):
#         for c in range(100):
#             # start_point = arr[99][answer]
#             for dr, dc in [[0,1],[0,-1],[-1,0]]:
#                 # for i in range(1,3):
#                 nr , nc = r + dr , c + dc
#                 if 0<=nr<100 and 0<=nc<100:
#                     if arr[nr][nc] == 1:
#                         start_point = arr[nr][nc]
#
#     print(start_point)

import sys

sys.stdin = open('input_05.text')
T = int(input())

for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(100)]

    answer = 0
    for i in range(100):
        if arr[99][i] == 2:
            answer = i
            break  # 2는 하나뿐이라고 가정하고 break로 종료

    c = answer  # 시작 지점
    print(answer)

    for r in range(98, -1, -1):  # 99에서 1까지 위로 한 칸씩 이동
        # 왼쪽으로 갈 수 있으면 왼쪽 끝까지
        # if c >= 0 and arr[r][c - 1] == 1:
        while c >= 0 and arr[r][c - 1] == 1:
            c -= 1
        # 오른쪽으로 갈 수 있으면 오른쪽 끝까지
        # elif c <= 99 and arr[r][c + 1] == 1:
        while c <= 99 and arr[r][c + 1] == 1:
            c += 1
        # 위로 이동은 for 루프에 의해 자동 처리됨

    print(f"#{tc} {c}")
