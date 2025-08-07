import sys
sys.stdin = open('input_1.text')

T = int(input())
for tc in range(1, T + 1):
    entire , A , B = map(int , input().split())
    cnt_A = cnt_B = 0 # A , B가 페이지 찾기를 시도한 횟수를 저장할 변수 선언
    left_p , right_p = 1, entire # 좌측 페이지, 우측 페이지 할당

    while left_p <= right_p: # 좌측페이지가 우측과 같아지면 종료
        cnt_A += 1 # 매 while문이 작동할때마다 페이지 찾기를 시도하므로 여기서 카운트를 셈
        med = int((left_p+right_p)/2) # 중앙페이지
        if med == A: # 바로 찾아버리면 종료
            break
        elif A > med: # 찾아야할 페이지가 중앙보다 크면
            left_p = med # 좌측을 중앙으로
        else:
            right_p = med # 그 반대의 경우에는 우측을 중앙으로

    left_p2, right_p2 = 1, entire # B의 경우 연산이므로 변수를 따로 선언
    while left_p2 <= right_p2: # 원리는 위와 동
        cnt_B += 1
        med = int((left_p2+right_p2)/2)
        if med == B:
            break
        elif B > med:
            left_p2 = med
        else:
            right_p2 = med

    if cnt_A > cnt_B: # A 의 횟수가 더 크면
        print(f'#{tc} B') # B가 이김
    elif cnt_A < cnt_B:
        print(f'#{tc} A') # 그 반대는 A가 이김
    else:
        print(f'#{tc} 0') # 동률이면 0을 준다.
