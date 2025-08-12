# import sys
# sys.stdin = open('text.txt')
# T = int(input())
#
# pairs = {')': '(', ']': '[', '}': '{'} # 여러개의 괄호를 딕셔너리로 선언. 닫는 괄호를 키, 여는걸 값으로
# def find(list_1):
#     stack = [] # 빈 스택 선언. 크기 조절 안해도 됨
#     ans = 1 # 상태. 1이면 괄호가 올바름. 0이면 아님
#     for i in list_1:
#         if i in '([{': # 문자열 안에 ([{ 셋중에 하나가 있을시
#             stack.append(i) # 그걸 stack 리스트에 추가
#         elif i in ')]}': # 이제 닫는 괄호 조사
#             if not stack or stack[-1] != pairs[i]: #스택이 비어있거나, 마지막 여는 괄호가 닫는 괄호랑 매칭이 안될시
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


import sys
sys.stdin = open('text.txt')
T = int(input())
for tc in range(1, 1+T):
    arr = input()
    stack = []
    ans = 1

    for i in arr: # 문자열 조사
        if i == '(': # ( 이면
            stack.append(i) # 스택에 쌓고
        elif i == ')': # ) 이면
            # 괄호 종류가 1개일때는 or 뒤에 필요x
            if not stack: #or stack[-1] != '(': # 스택이 비었거나, 또는 스택 마지막이 (랑 다른지 확인
                ans = 0 # if문에 걸리면 상태는 0
                break # 멈춤
            stack.pop() # 아니면 stack에 쌓인거 끝부터 제거

    if not ans or stack: # ans가 0이거나 stack이 비어있지 않으면
        print(f'#{tc} -1') # -1을 출력
    else:
        print(f'#{tc} 1') # 그 외는 1을 출력
