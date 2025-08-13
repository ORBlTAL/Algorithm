# N : 사람수 , M : 만드는데 걸리는 시간 , K : M초 동안 만든 붕어빵의 개수

import sys
sys.stdin = open('input_6.txt')
T = int(input())
for tc in range(1, 1 + T):
    N , M , K = map(int,input().split())
    time = list(map(int, input().split()))
    print(N,M,K)
    # print(time)
    """
    불가능한 경우 1 : 빵 다 만들기도 전에 손님이 먼저 온 경우
    불가능한 경우 2 : 빵 다 만들고 다음 빵 만들기 전에 손님이 먼저 온 경우 
    """