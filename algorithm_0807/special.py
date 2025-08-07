import sys
sys.stdin = open('input_0.text')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N-1): # 선택정렬 기법을 활용해서 입력받은 리스트를 순서대로 정렬
        min_idx = i
        for j in range(i+1 , N):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i] , arr[min_idx] = arr[min_idx] , arr[i]

    new_arr = [] # 인덱스를 활용해서 for문으로 문제에 순서에 맞게 넣기
    # 10 1 , 9 2, 8 3 .. 이런식으로 넣음
    for i in range(1, 6):
        new_arr.append(arr[-i])
        new_arr.append(arr[i-1])
        # new_arr.append(arr[-1])
        # new_arr.append(arr[0])
        # new_arr.append(arr[-2])
        # new_arr.append(arr[1])
        # new_arr.append(arr[-3])
        # new_arr.append(arr[2])
        # new_arr.append(arr[-4])
        # new_arr.append(arr[3])
        # new_arr.append(arr[-5])
        # new_arr.append(arr[4])
    print(f'#{tc}', *new_arr)


 # append 없이 하는 방법을 찾아서 시도
# 지그재그??
