import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, 1 + T):
    arr = list(map(int, input().split()))

    n = len(arr) # 정수 리스트의 길이
    found = False # 합이 0이 되는게 존재하는지 안하는지 판별
    for i in range(1, 1 << n): # 전체의 부분집합을 봐야하니 2^10
        sum_val = 0 # 합구하는 변수 초기화
        for j in range(n): # 모든 원소 개수 만큼 반복
            if i & (1 << j): # 비트 연산을 통해 부분집합 탐색 시작
                sum_val +=arr[j] # 합을 저장

        if sum_val == 0: # 합이 0일시
            found = True # 상태를 True로 변환
            break
    if found: # True면 1, 아니면 0 출력
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)