import sys
sys.stdin = open('input_1.text')


T = int(input()) # input txt 에서 맨 처음 줄 문자열을 int형으로 바꿔서 가져옴 (행의 개수)
#
for test_case in range(1, T + 1): # swea에서 1부터 시작하므로 1 ~ T+1
    N = int(input()) # 2번째 줄에 적힌 문자열을 int로, 첫째행 데이터의 개수
    numbers = list(map(int, input().split())) # 하나씩 가져온 문자열 데이터를 int형 변환, 리스트로 저장
    max_num = numbers[0] # 최대값 초기화
    min_num = numbers[0] # 최저값 초기화

    for num in numbers: # 리스트 순회
        if num > max_num: # 조회된 값이 max보다 크면
            max_num = num # 그 값이 최대
        if num < min_num: # 조회된 값이 min 보다 작으면
            min_num = num # 그 값이 최저
    list_minus = max_num - min_num # 최대와 최소의 차이
    print(f"#{test_case} {list_minus}") # swea 형식에 맞게 f-string으로 출력












# import sys
# sys.stdin = open('input.txt')
#
#
# T = int(input()) # test case의 수
# #
# for tc in range(1, T + 1): # 이렇게 해야 T 개수 만큼 전체 코드가 돈다 , swea는 0부터 출력을 안해서 1부터 시작
#     N = int(input())
#     matrix = []
#     numbers = list(map(int, input().split()))
#     print(f"Test case #{tc}:")
#     print(numbers)
