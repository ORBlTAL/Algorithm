import sys
from collections import deque
sys.stdin = open('input_1.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))  # C[i] = i번째(1-based로는 i+1) 피자의 초기 치즈

    # 화덕 큐: (피자번호, 남은치즈)
    oven = deque()
    i = 0
    while i < N and i < M:
        oven.append((i + 1, C[i]))
        i += 1

    next_idx = i  # 다음에 넣을 피자의 0-based 인덱스

    # 큐에 피자가 1개 남을 때까지 진행
    while True:
        if len(oven) == 1:
            answer = oven[0][0]  # 남아있는 피자 번호
            break

        num, cheese = oven.popleft()
        cheese //= 2

        if cheese == 0:
            # 이 자리에 대기 피자를 투입(있으면)
            if next_idx < M:
                oven.append((next_idx + 1, C[next_idx]))
                next_idx += 1
            # 없으면 그냥 빈 자리가 되어 큐 크기가 줄어듦
        else:
            # 아직 안 녹았으면 다시 넣기
            oven.append((num, cheese))

    print(f"#{tc} {answer}")


















 # 좀 수정하면 될 꺼 같은디....
T = int(input())
for tc in range(1, 1 + T):
    N , M  = map(int, input().split())
    arr = list(map(int, input().split()))
    que = arr[:N]
    new = arr[N:]
    mem = []
    state = True
    while state:
        for i in range(len(que)):
            que[i] //= 2
            if que[i] == 0:
                que[i] = 'done'
                mem.append(i)
                que.append(new[0])
        if all(i in ('done') for i in que):
            break
    print(mem[-1])




