import sys
sys.stdin = open('input_2.text')
T = 10
for tc in range(1 , T + 1):
    _ = int(input()) # 무시
    arr = [list(map(int, input().split())) for _ in range(100)] # 100x100 배열 받아옴
    max_11_list = [] # 행의합들 저장
    max_12_list = [] # 열의합들 저장
    for r in range(100):
        sum_11 = 0
        for c in range(100):
            sum_11 += arr[r][c] # 각 행마다 합을 구해서
        max_11_list.append(sum_11) # 리스트에 저장
    max_11 = max(max_11_list) # 최대값 구함

    for c in  range(100):
        sum_12 = 0
        for r in range(100):
            sum_12 += arr[r][c] # 각 열마다 합을 구해서
        max_12_list.append(sum_12) # 리스트에 저장
    max_12 = max(max_12_list) # 최대값 구함

    sum_21 = 0 # 정방향 대각선의 합 변수
    for r in range(100):
        sum_21 += arr[r][r] # 누적합을 구함

    sum_22 = 0 # 역방향 대각선의 합 변수
    for r in range(100):
        sum_22 += arr[r][99-r] # 누적합을 구함

    result = [] # 4개 영역의 최대값들 저장 리스트
    result.extend([max_11,max_12,sum_21,sum_22]) # 리스트에 넣음
    print(f"#{tc} {max(result)}") # 최대값 출력