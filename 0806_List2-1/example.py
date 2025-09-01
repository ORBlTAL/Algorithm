import sys
sys.stdin = open('input_0.text')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    result = 0
    arr = [list(map(int , input().split())) for _ in range(N)]
    for r in range(N):
        for c in range(N):
            for dr, dc in [[0,1],[1,0],[0,-1],[-1,0]]:
                nr, nc = r + dr , c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    result += abs(arr[nr][nc] - arr[r][c])

    print(f"#{T} {result}")