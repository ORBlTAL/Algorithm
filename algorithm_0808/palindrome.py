import sys
sys.stdin = open('input_1.txt')

T = int(input())
for tc in range(1, 1 + T):
    N , M = map(int , input().split())

    text = [input() for _ in range(N)]  # N줄 읽기
    # print(text)
    # for i in text:
    #     L = N
    #     for j in range(N-M+1):
    #         if i[j:M+j] == i[-(L-M+j+1):-(L-j+1):-1]: # and len(text) == M  일치하는 부분만 출력은 어떻게?.....
    #             print(f'#{tc}' ,i[j:M+j] )
    #
    # for j in range(N):
    #     col = ''
    #     for i in range(N):
    #         col += text[i][j]
    #         L = N
    #         for j in range(N - M + 1):
    #             if col[j:M+j] == col[-(L - M - j + 1) : -(L + 1 - j) : -1]:
    #                 print(f'#{tc}', col[j:M+j])

# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     text = [input().strip() for _ in range(N)]

    # 가로 검사
    for row in text:
        L = N  # 행 길이
        for j in range(L - M + 1):
            if row[j:M + j] == row[-(L - M - j + 1): -(L + 1 - j): -1]:
                print(f'#{tc}', row[j:M + j])

    # 세로 검사
    for c in range(N):
        col = ''  # 열 문자열 누적 시작
        for r in range(N):
            col += text[r][c]  # 한 글자씩 추가
        L = N # 열 길이
        for j in range(L - M + 1):
            if col[j:M + j] == col[-(L - M - j + 1): -(L + 1 - j): -1]:
                print(f'#{tc}', col[j:M + j])

# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     board = [input().strip() for _ in range(N)]
#
#     ans = None
#     # 가로
#     for r in range(N):
#         row = board[r]
#         for c in range(N - M + 1):
#             s = row[c:c+M]
#             if s == s[::-1]:
#                 ans = s
#                 break
#         if ans:
#             break
#
#     print(f'#{tc} {ans}')