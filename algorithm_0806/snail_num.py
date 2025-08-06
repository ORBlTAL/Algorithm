# import sys
# sys.stdin = open('input_3.text')
#
# T = int(input())
# for tc in range(1 , T + 1):
#     N = int(input())
#     arr = [[0] * N for _ in range(N)]
#     if N == 1:
#         print(f'#{tc} \n {1}')
#     else:
#         dr = [-N//2 , -N//2 , N//2 ,N//2]
#         dc = [-N//2 , N//2, N//2, -N//2]
#         for r in range(N-1):
#             for c in range(N-1):
#                 for i in range(4):
#                     nr = N//2 + dr[i]
#                     nc = N//2 + dc[i]
#                     if 0 <= nr < N and 0 <= nc < N:
#                         for j in range(1, N**2+1):
#                             arr[nr][nc] = j
#         print(arr)
#

# 입력 파일 읽기
import sys
sys.stdin = open('input_3.text')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r, c = 0, 0
    direction = 0

    for num in range(1, N*N + 1):
        arr[r][c] = num
        nr, nc = r + dr[direction], c + dc[direction]

        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            r, c = nr, nc
        else:
            direction = (direction + 1) % 4
            r += dr[direction]
            c += dc[direction]

    print(f'#{tc}')
    for row in arr:
        print(' '.join(map(str, row)))
