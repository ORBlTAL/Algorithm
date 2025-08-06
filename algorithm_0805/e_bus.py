# N//K 부분으로 인한 오류로 10개중 7개 통과. N//K 가 아닌 경우에만 추가해주는
# 문구를 작성하면 될 꺼 같은데 구현이 안되는 중
# import sys
# sys.stdin = open("input_2.text")
#
# T = int(input())
# for test_case in range(1,T+1):
#     K,N,M = map(int , input().split())
#     arr = list(map(int, input().split()))
#
#     state = True # 초기 상태
#     if M < N//K :  # M 값이 N//K 보다 작으면 도달 불가
#         state = False
#
    # if arr[0] > K: # 초기 정류소가 K보다 길면 못감
    #     state = False
    #
    # if N - arr[-1] > K: # 종점이 그 이전 정류소 보다 멀면 못감
    #     state = False
    #
    # for i in range(1, len(arr)): # 충전소 간의 거리가 K보다 길면 못감
    #     if arr[i] - arr[i-1] > K:
    #         state = False
    #         break

#     if state:
#         print(f"#{test_case} {N//K}") # True 상태가 유지되면 이걸 출력
#             # 여기서 문제가 생기는 이유는 만약 K=4, N=10, 이러면 2번 충전해도 될때가 있고, 3번 충전이 필요할 때도 있음
#             # 지금준 txt 파일에 나온 값 이외의 상황에서도 이러한 문제가 발생할 수 있음.
#     else:
#         print(f"#{test_case} 0") # 아니면 0

"""
일단 arr 배열 내에서 M 값이 N//K 보다 크거나 같아야 된다. 
또한 충전소들간의 거리인 arr[i] - arr[i-1]이 K값보다 커야한다. 
이 2가지 조건이 충족되어야만 전기 버스는 원하는 거리까지 갈 수 있고, 이때 최소한의 충전횟누는 N//K 이다.
첫 충전소의 위치가 K보다 커도 충전이 안되므로 못간다.
마지막 충전소에서부터 최종까지도 K보다 크면 못간다. 
위 조건 외에는 무조건 못가므로 0을 출력하면 된다. 
"""


import sys
sys.stdin = open("input_2.text")

T = int(input())
for test_case in range(1,T+1):
    K, N, M = map(int , input().split())
    arr = list(map(int, input().split()))

    charge = 0 # 충전 횟수 저장
    last = 0 # 마지막 충전 위치

    state = True # 도착 가능여부
    for i in range(M): # 충전소를 하나씩 조히
        if arr[i] - last > K: # 마지막 충전소부터 현재 충전소까지 거리가 K 이상이면 못감
            state = False # 상태를 False로 바꾸고 종료
            break
        # 2차 체크. 다음 충전소 도달 가능 여부를 판단
        if i < M - 1 and arr[i+1] - last > K: # 다음 충전소가 마지막 충전 거리 보다 길다면
            last = arr[i] # 마지막 충전 위치를 현재 충전소로 갱신
            charge += 1 # 충전했으니 +1
    # 마지막 충전 위치에서 종점까지 도달 가능한지 체크
    if state:
        if N - last > K: # 마지막 충전 위치에서 종점까지 거리가 K를 초과한다면... 충전 해야함
            if N - arr[-1] > K: # 마지막 충전소에서 종점까지 거리가 K보다 길면 못감
                state = False
            else:
                charge += 1 # 충전에서 갈 수 있는 경우에는 충전, +1

    if state:
        print(f"#{test_case} {charge}") # 상태가 참이면 충전횟수 출력
    else:
        print(f"#{test_case} 0") # 거짓이면 0 출력
