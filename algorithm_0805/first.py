# import sys
# sys.stdin = open("input_1.text")
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N, M = map(int , input().split())
#     arr = list(map(int, input().split()))
#
#     max_sum = min_sum = 0 # 최대 최소를 0으로 초기화
#     for i in range(M): # 처음 M 크기 만큼의 합을 최대, 최소의 합이라 선언
#         max_sum += arr[i]
#         min_sum += arr[i]
#
#     for i in range(N - M + 1): # 구간이 M개일시 M묶음씩 전체를 순회하니 그 개수는 N - M + 1
#         temp = 0 # 최대 최소를 반영할 변수 0 선언
#         for j in range(i, i + M): # M 묶음씩 순회
#             temp += arr[j] # 합을 구함
#         if temp < min_sum: # 합이 최소보다 작을시
#             min_sum = temp # 최소합으로 할당
#         if temp > max_sum: # 합이 최대보다 클시
#             max_sum = temp # 최대합으로 할당
#
#     print(f"#{test_case} {max_sum - min_sum}") # 문제 조건에 맞게 출력하기위해 f-string으로 출력



import sys
sys.stdin = open('input_1.text')

T = int(input())
for test_case in range(1, 1 + T):
    N , M = map(int, input().split())
    arr = list(map(int, input().split()))

    max_v = min_v = 0
    for i in range(M):
        max_v += arr[i]
        min_v += arr[i]

    for i in range(N - M  + 1):
        temp = 0
        for j in range(i, i+M):
            temp += arr[j]
        if max_v < temp:
            max_v = temp
        if min_v > temp:
            min_v = temp
    print(f"#{test_case} {max_v-min_v}")























