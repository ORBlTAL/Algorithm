import sys
sys.stdin = open('input_3.txt')
T = int(input())
for tc in range(1, 1 + T):
    arr = [list(map(int, input().split())) for _ in range(9)]

    cnt_1 = cnt_2 = cnt_3 = 0 # 한행의 모든 수의 합이 45가 아니면 cnt_1을 세서 스도쿠가 성립 안된다는걸 표시
    for i in range(9):
        sum_val_1 = 0
        for j in range(9):
            sum_val_1 += arr[i][j]
        if sum_val_1 != 45:
            cnt_1 +=1

    for j in range(9): # 한열의 모든 수의 합이 45가 아니면 cnt_2을 세서 스도쿠가 성립 안된다는걸 표시
        sum_val_2 = 0
        for i in range(9):
            sum_val_2 += arr[i][j]
        if sum_val_2 != 45:
            cnt_2 +=1

    sum_val_3 = 0
    for i in range(0,7,3): # 전체 스도쿠에서 3x3 영역을 돌면서 모든 수의 합이 45가 아니면 cnt_3을 세서 스도쿠가 성립 안된다는걸 표시
        for j in range(0,7,3):
            sum_val_3 = arr[0+i][0+j] + arr[0+i][1+j] + arr[0+i][2+j] + arr[1+i][0+j] + arr[1+i][1+j] + arr[1+i][2+j] + arr[2+i][0+j] + arr[2+i][1+j] + arr[2+i][2+j]
            if sum_val_3 !=45:
                cnt_3 +=1

    if (cnt_1 + cnt_2 + cnt_3) ==0: # 세개의 cnt 합이 0이면 스도쿠 성립
        print(f'#{tc}',1) # 1로 출력
    else:
        print(f'#{tc}',0) # 그 외는 모두 성립이 안되니 0으로 출력
