# import sys
# sys.stdin = open('input2.txt')
# T = int(input())
# arr = range(1,13)
# n = len(arr)
# for tc in range(1, 1 + T):
#     N , M = map(int, input().split())
#     result = 0 # 결과 저장 변수
#     for i in range(1 << n):
#         sum_val = 0 # 부분집합 원소들의 합
#         cnt = 0 # 부분집합의 원소의 개수를 저장
#         for j in range(n):
#             if i & (1 << j): # 여기서  i & (1<<j) 가 성립 될 때만 1부터 12의 부분집합 중 하나가 나오게 된다.
#                 sum_val+=arr[j] # 그때의 합과
#                 cnt +=1 # 원소의 개수를 더함
#         if cnt == N and sum_val == M: # 원소가 N 개고, 원소 합이 K인 부분집합을 찾는 과정
#             result +=1 # 찾으면 + 1
#     print(f'#{tc}', result)
