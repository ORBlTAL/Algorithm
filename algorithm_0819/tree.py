import sys

sys.stdin = open('input_2.txt')
# T = int(input())
# for tc in range(1, 1 + T):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     arr.sort()
#     fisrt = arr[0]
#     # state = True
#     # for i in arr:
#     #     if i != fisrt:
#     #         state = False

#     sum_val = 0
#     max_val = max(arr)
#     for i in range(N):
#         if arr[i] == max_val:
#             continue
#         else:
#             sum_val +=max_val - arr[i]
#     # print(sum_val)
#     cnt1 = 0
#     while sum_val > 0:

#         if cnt1 % 2 == 0:  # -1 차례
#             if sum_val >= 1:
#                 sum_val -= 1
#         else:  # -2 차례
#             if sum_val >= 2:
#                 sum_val -= 2
#         cnt1 += 1
#     print(cnt1)


#     # if state:
#     #     print(f'#{tc}', 0)
#     # else:
#     #     print('d')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_val = max(arr)

    needs = [max_val - h for h in arr if h < max_val]
    total_need = sum(needs)

    left, right = 0, 10 ** 5
    ans = right
    while left <= right:
        mid = (left + right) // 2
        grow = (mid // 2) * 3 + (mid % 2)

        if grow >= total_need:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    print(f'#{tc}', ans)
