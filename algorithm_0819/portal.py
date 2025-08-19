import sys
sys.stdin = open('input_1.txt')
T = int(input())

for tc in range(1 , 1+T):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    cnt2 = 0
    while cnt < N:
        i = cnt
        if i+1 >= N and i+1 == 0:
            break
        elif i+1 < N:
            for j in range(arr[i+1]-1,cnt+1):
                cnt2 +=1
        cnt +=1

    cnt3 = 0
    for i in arr:
        if i != 0:
            cnt3 +=1
    # print(cnt3)

    print(f'#{tc}', cnt2+cnt3-1)
    #


    # 꼭 다시 풀어볼것!!
    # 수정된 코드
    # i = 0
    # cnt2 = 0  # ->
    # while i < N:
    #     i += 1
    #     if i >= N and i == 0:
    #         break
    #     elif i == 1:
    #         cnt2 += 1
    #     elif 1 < i < N:
    #         for _ in range(arr[i - 1] - 1, i):
    #             cnt2 += 1
    #             print(tc, cnt2)
    #
    # cnt3 = 0  # <-
    # for i in arr:
    #     if i != 0:
    #         cnt3 += 1
    #
    # print(f'#{tc}', cnt2 + cnt3)