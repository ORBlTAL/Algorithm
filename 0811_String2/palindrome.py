# import sys
# sys.stdin = open('input_3.txt')
# T = 10
# for tc in range(1, 1 + T):
#     N = int(input())
#     arr = [input() for _ in range(8)]
#     result1 = 0
#     result2 = 0
#     cnt1 = 0
#     cnt2 = 0
#     for i in range(8):
#         for j in range(8-N+1):
#             # for k in range(N):
#             if arr[i][j:N+j] == arr[i][N-1+j:-1+j:-1]:
#                 cnt1 +=1
#     print(cnt1)
#
#     # for j in range(8):
#     #     for i in range(8-N+1):
#     #         if arr[i:N+i][j] == arr[N-1+i:-1+i:-1][j]:
#     #             cnt2 +=1
#     # 첫 번째(가로)는 그대로 두고
#
#     # 두 번째(세로)만 이렇게:
#     cnt2 = 0
#     for j in range(8):  # 열 고정
#         col = ''.join(arr[i][j] for i in range(8))  # 열을 문자열로 읽기
#         for i in range(8 - N + 1):
#             if col[i:i + N] == col[i:i + N][::-1]:  # if 한 줄로 끝
#                 cnt2 += 1
#
#     print(cnt2)
#
#     # for j in range(8-N+1):
#     #     for i in range(8-N+1):
#     #         cnt = 0
#     #         for k in range(N):
#     #             if arr[k+i][k+j] == arr[N-k+i-1][N-k+j-1]:
#     #                 cnt +=1
#     #         if cnt == N:
#     #             result2 +=1
#
#     # print(result1 , result2)


import sys
sys.stdin = open('input_3.txt')
T = 10
for tc in range(1, T + 1):
    N = int(input().strip())
    arr = [input().strip() for _ in range(8)]
    result = 0

    for i in range(8): # 행 순회
        row = arr[i] # 각 행을 row로 할당
        for j in range(8 - N + 1): # 열 순회
            w = row[j:j+N] # N 크기만큼 행을 분석
            if w == w[::-1]: # N크기의 행과 N크기의 역행이 같을 경우
                result += 1 # 개수를 센다

    for j in range(8): # 열 순회
        col = "" # 열을 저장할 변수 선언
        for i in range(8): # 행 순회
            col += arr[i][j] # 한 열씩 col에 할당
        for i in range(8 - N + 1): # N 크기만큼 열을 분석
            if col[i:i + N] == col[i:i + N][::-1]: # 서로 간에 행은 동일, 열만 역순일 경우
                result += 1 # 개수를 센다

    print(f"#{tc} {result}") # 가로, 세로 기존과 역이 같은 문자열 개수 출력력