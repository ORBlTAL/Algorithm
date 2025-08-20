import sys
from collections import  deque
sys.stdin = open('input_0.txt')

T = int(input())
for tc in range(1, 1 + T):
    N , M = map(int, input().split())
    arr = list(map(int , input().split()))
    dq = deque(arr)
    for _ in range(M):
        left = dq.popleft()
        dq.append(left)
    print(f'#{tc}',dq[0])



















    # def app(arr, value):
    #     arr.append(value)
    #
    #
    # def po(arr):
    #     return arr.pop(0)
    #
    #
    # T = int(input())
    # for tc in range(1, 1 + T):
    #     N, M = map(int, input().split())
    #     arr = list(map(int, input().split()))
    #     for _ in range(M):
    #         value = po(arr)
    #         app(arr, value)
    #     print(f'#{tc}', arr[0])







    # print(f'#{tc}',arr[M % N])