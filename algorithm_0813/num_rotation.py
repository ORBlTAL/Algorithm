import sys
import copy
sys.stdin = open('input_1.txt')
T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 깊은 복사를 이용해 원본 배열 복사
    arr_90 = copy.deepcopy(arr) # 90도
    arr_180 = copy.deepcopy(arr) # 180도
    arr_270 = copy.deepcopy(arr) # 270도

    # 인덱스를 해당 각도만큼 회전했을때 출력에 맞게 순서를 수정
    for i in range(N):
        for j in range(N):
            arr_90[i][j] = arr[N-1-j][i]
            arr_180[i][j] = arr[N-1-i][N-1-j]
            arr_270[i][j] = arr[j][N-1-i]

    # 출력 양식에 맞게 같은 각도 끼리는 공백없이 붙이고, 다른 각도 끼리는 한칸 띄움. 그리고 옆으로 나열해서 출력
    print(f"#{tc}")
    for i in range(N):
        s90 = ''.join(map(str, arr_90[i]))
        s180 = ''.join(map(str, arr_180[i]))
        s270 = ''.join(map(str, arr_270[i]))
        print(s90, s180, s270)
