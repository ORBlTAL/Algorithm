import sys
sys.stdin = open('input_2.text')
T = int(input())

for tc in range(1, 1 + T):
    N = int(input())
    arr = list(map(int, input().split()))

    # 버블정렬
    # for i in range(N):
    #     for j in range(N-i-1):
    #         if arr[j] > arr[j+1]:
    #             arr[j] , arr[j+1] = arr[j+1], arr[j]
    # print(f'#{tc}', *arr)

    # 선택 정렬
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i] , arr[min_idx] = arr[min_idx] , arr[i]

    print(arr)
