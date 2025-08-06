import sys
sys.stdin = open('input_1.text')
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)] # 10x10 크기의 모든 값이 0인 리스트 선언
    cnt = 0 # 겹치는 부분의 개수를 셀 변수 선언
    for _ in range(N): # 색칠 영역이 생길때마다 면적에서 겹치는걸 고려해야 하므로
        x1,y1,x2,y2,_ = map(int,input().split()) # 좌표값을 따로 받음, 색상은 버림
        for r in range(x1 , x2+1): # x좌표 범위, range는 마지막을 빼므로 +1 해서 길이 맞춤
            for c in range(y1, y2+1): # y좌표 범위
                if arr[r][c] == 0: # 해당 좌표 면적안에 영역이 0이면
                    arr[r][c] =1 # 1로 바꿔줌
                elif arr[r][c] == 1: # 좌표면적안에 값이 1이면
                    cnt +=1 # 그만큼 개수를 센다
    print(f'#{tc} {cnt}') # 형식에 맞게 출력





