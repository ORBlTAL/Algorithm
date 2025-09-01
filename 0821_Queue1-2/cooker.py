# import sys
# from itertools import permutations
# sys.stdin = open('input_3.txt')
# T = int(input())
# for tc in range(1, 1 + T):
#     N = int(input())
#     arr= [list(map(int, input().split())) for _ in range(N)]
"""
    순열로 풀꺼면 4개중 2개를 골라서 기존 순서, 반전된 순서 둘 다 더해줘야 A , B가 나온다.
     A가 2개 고르고, B 는 A가 안고른 2개를 배정 
     baby_gin 참고 
"""

import sys
from itertools import combinations
sys.stdin = open('input_3.txt')

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # (i<j) 시너지 미리 합산
    pair = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            pair[i][j] = arr[i][j] + arr[j][i]

    ans = float('inf')

    # A 그룹 뽑기 (대칭 제거 위해 0 포함 필수)
    for group_a in combinations(range(N), N//2):
        if 0 not in group_a:
            continue

        # A 시너지 합
        sumA = 0
        for i, j in combinations(group_a, 2):
            sumA += pair[i][j]

        # B 그룹 (보수 집합)
        used = [False] * N
        for x in group_a:
            used[x] = True
        group_b = []
        for i in range(N):
            if not used[i]:
                group_b.append(i)

        # B 시너지 합
        sumB = 0
        for i, j in combinations(group_b, 2):
            sumB += pair[i][j]

        ans = min(ans, abs(sumA - sumB))
        if ans == 0:   # 0이 최소니까 break
            break

    print(f'#{tc} {ans}')
