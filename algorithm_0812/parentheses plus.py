import sys
sys.stdin = open('input_5.txt')
T = 10

pair = {')':'(' , ']':'[' , '}':'{' , '>':'<'} # 괄호 딕셔너리 선언

for tc in range(1, 1 + T):
    N = int(input())
    arr = list(input())
    stack = [] # 스택을 저장할 빈 리스트 스택 선언
    value = 1 # 스택이 비면 1, 차있으면 0이라 판단할 value 선언
    for ch in arr:
        if ch in '([{<': # 문자열 중에서 해당 괄호가 속하는 문자이면
            stack.append(ch) # 그 문자를 리스트에 저장
        elif ch in ')]}>': # 문자열 중에서 해당 괄호가 속하는 문자이면
            if not stack or stack[-1] != pair[ch]: # 스택이 비었거나, 딕셔너리랑 매칭이 안맞을 시
                value = 0 # 문제 조건에 부합하지 않으므로 0으로 처리
                break # 멈춤
            stack.pop() # if가 아닐시 pop으로 스택 지움
        else:
            continue
    if stack:
        value = 0
    print(f'{tc}',value)
