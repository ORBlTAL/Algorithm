import sys
sys.stdin = open('input_4.txt')
T = 10
for test in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(100)]
    max_1 = 0 # 최대 길이 저장 변수
    max_2 = 0 # 최대 길이 저장 변수
    for i in range(100): # 행 탐색
        for j in range(100): # 열 탐색
            arr_len = 0 # 회문 길이
            for k in range(2, 101-j): # 길이가 2 부터 100일 때 까지의 모든 회문을 탐색
                a = arr[i][0+j:k+j] # 한칸식 옆으로 이동하면서 탐색하고 한 행을 다 돌면 다음행으로
                if a == a[::-1]: # 문자열이 역과 같은 경우
                    arr_len = len(a) # 그 때의 길이를 할당
            if max_1 < arr_len: # 최대값만 뽑아오기 위해 max_1과 비교
                max_1 = arr_len

    transposed_arr = list(map(list, zip(*arr))) # 기존 2차원 배열을 전치해서 새로운 배열 선언
    for i in range(100): # 나머지 방법은 위와 동일
        for j in range(100):
            arr_len = 0
            for k in range(2, 101-j):
                a = transposed_arr[i][0+j:k+j]
                if a == a[::-1]:
                    arr_len = len(a)
            if max_2 < arr_len:
                max_2 = arr_len
    if max_1 > max_2: # max_1이 더 클시 max_1 출력
        print(f'#{N}',max_1)
    else: # 아니면 max_2 출력
        print(f'#{N}',max_2)



