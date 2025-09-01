import sys
sys.stdin = open('input_2.txt')
T = int(input())
for tc in range(1, 1 + T):
    arr = list(input())
    i = 0  # 0 부터 시작
    while i < len(arr) - 1:  # 앞뒤 2개씩 반복 문자 검사
        if arr[i] == arr[i + 1]:  # 현재 문자와 다음 문자가 같으면
            arr.pop(i)  # 현재 문자 제거
            arr.pop(i)  # 같은 자리에서 다시 제거,즉 원래 i+1이었던 문자 제거
            if i > 0:  # 앞쪽 문자가 새로 생긴 쌍이 될 수 있으므로
                i -= 1  # 한 칸 뒤로 돌아가 재검사
        else:
            i += 1  # 같지 않으면 다음 문자로 이동

    print(f'#{tc}',len(arr))



# s = input().strip()

# stack = []
# for ch in s:
#     if stack and stack[-1] == ch:
#         stack.pop()      # 바로 이전과 같으면 제거 (짝 지워짐)
#     else:
#         stack.append(ch) # 다르면 쌓기
#
# result = ''.join(stack)
# print(result)            # 남은 문자열 (전부 지워지면 빈 문자열)
