import sys
sys.stdin = open('input_4.text')

T = int(input())
for test_case in range(1, T + 1):
    _ = int(input()) # 필요 없음
    num = int(input()) # 정수로 받음
    current_cnt = 0 # 정수에서 1로 이루어진 구간의 1의 개수를 세는 변수
    max_cnt = 0 # 최대 1의 개수를 저장하는 변수
    while num > 0: # num을 10으로 나눠가면서 진행. 0되면 종료
        if num % 10 == 1: # 나머지가 1이면
            current_cnt+=1 # 1의 개수를 센다
            if max_cnt < current_cnt: # 개수를 세면서 최대값 갱신
                max_cnt = current_cnt
        else: # 나머지가 0이면
            current_cnt = 0 # 1의 개수 0으로 초기화. m
        num = num //10 # 10으로 나눈 몫을 다시 num으로
    print(f"#{test_case} {max_cnt}")