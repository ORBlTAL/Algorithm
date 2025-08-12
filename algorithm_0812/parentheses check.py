import sys
sys.stdin = open('input_1.txt')
T = int(input())
pair = {')':'(','}':'{' } # 탐지하는 괄호 문자 딕셔너리로 선언
for tc in range(1, 1+T):
    arr = input()
    value = 1 # 스택이 남으면 0 아니면 1
    stack = [] # 빈 스택 리스트 선언
    for i in arr:
        if i in '({': # 문자열에서 문자 하나씩 조사할 때 (,{ 인 경우
            stack.append(i) # 스택 리스트에 저장
        elif i in ')}': # ),} 인경우
            if not stack or stack[-1] != pair[i]: # 스택이 비어있거나, 스택 리스트 마지막이랑 불일치할 경우
                value = 0 # value를 0으로
                break # 이미 문제가 생겼으므로
            stack.pop() # if 에 안걸리면 스택을 한개씩 지움
        else:
            continue # 괄호 기호 이외의 문자들은 무시
    if stack: # 위의 elif if 문 이외에도 마지막까지 갔을 때 stack이 안비워지면
        value = 0 # value를 0으로
    print(f'#{tc}', value)



# def find(list_1):
#     stack = [] # 빈 스택 선언. 크기 조절 안해도 됨
#     ans = 1 # 상태. 1이면 괄호가 올바름. 0이면 아님
#     for i in list_1:
#         if i in '([{': # 문자열 안에 ([{ 셋중에 하나가 있을시
#             stack.append(i) # 그걸 stack 리스트에 추가
#         elif i in ')]}': # 이제 닫는 괄호 조사
#             if not stack or stack[-1] != pair[i]: #스택이 비어있거나, 마지막 여는 괄호가 닫는 괄호랑 매칭이 안될시
#                 ans = 0 # 상태는 0으로
#                 break # 이미 틀렸먹었으니 break
#             stack.pop() # if문 외에는 괄호가 올바르니 제거해주면 된다
#         else:
#             continue #과홀 외 문자는 무시
#     if stack: # 스택이 참일시, 즉 안에 뭔가 있음. 괄호가 모두 올바르게 배치되었다면 비어야 함
#         ans = 0
#     return ans # 반환
#
# for tc in range(1, 1+T):
#     arr = input()
#     print(f'#{tc}',find(arr)) # 괄호순서가 올바른지 아닌지 결과 출력
