import sys
from collections import deque
sys.stdin = open('input_2.txt')
T = 10
for tc in range(1, 1 + T):
    _ = int(input())
    arr = list(map(int, input().split()))
    dq = deque(arr)

    state = True
    while state:
        for i in range(5):
            dq[0] = dq[0] - (i+1)
            k = dq.popleft()
            dq.append(k)
            if dq[7] <= 0:
                dq[7] = 0
                state = False
                break
    print(f'#{tc}', *dq)

# for tc in range(1, 1 + T):
#     # 테스트 케이스 번호를 입력받음 (여기서는 필요 없지만, 문제 형식에 맞춤)
#     _ = int(input())
#
#     # 8개의 숫자를 deque로 변환하여 입력받음
#     arr = list(map(int, input().split()))
#     dq = deque(arr)
#
#     state = True
#     while state:
#         for i in range(5):
#             # 맨 앞 요소를 꺼내고
#             k = dq.popleft()
#             # 값을 감소시킴
#             k -= (i + 1)
#
#             # 값이 0보다 작거나 같으면 0으로 만듦
#             if k <= 0:
#                 k = 0
#                 dq.append(k)
#                 state = False  # 프로그램 종료를 위해 state를 False로 변경
#                 break  # 내부 for 루프를 종료
#
#             # 새로운 값을 맨 뒤에 추가
#             dq.append(k)
#
#     # 최종 결과를 출력 형식에 맞게 출력
#     print(f"#{tc}", *dq)