import sys
sys.stdin = open('input_3.text')

for test_case in range(1, 11): # 10가지 이니
    T = int(input()) # 덤프 횟수
    arr = list(map(int, input().split())) # 높이 리스트로 받아오기

    for _ in range(T):
        max_val = arr.index((max(arr))) # 최대값 구하기
        min_val = arr.index((min(arr))) # 최소값 구하기
        arr[max_val] -= 1 # 1씩 빼고
        arr[min_val] += 1 # 1씩 더하고

    print(f"#{test_case} {max(arr) - min(arr)}") # 마지막 덤프 실행 후 최대와 최소의 차이 구하기
    # print(arr[max_val] - arr[min_val]) ...? 왜 다르지?...