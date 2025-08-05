import sys
sys.stdin = open('input_2.text')

T = int(input())
print(T)
for test_case in range(1 , T + 1): #
    N = int(input())
    number = list(map(int, input()))
    count_num = {}

    for num in number:  # 입력 받은 수를 딕셔너리로 변환 해서 각 자리 수를 key, 개수를 values로
        if num not in count_num.keys(): # number에 저장된 num을 키로 선언
            count_num[num] = 1 # 키를 num으로, value를 1로 한 딕셔너리
        else:
            count_num[num] += 1 # 있을경우 value 값에 +1을 해서 해당 숫자의 개수 세기
    # print(count_num)

    value_list = list(count_num.values()) # 딕셔너리의 value값들(숫자 개수) 리스트로
    first_value = value_list[0] # 첫번째 개수값 선언

    decision = True # 개수가 같은지 다른지 확인하는 조건. 같으면 True, 다르면 False
    for val in value_list: # 리스트에 저장된 value값들 조회
        if val != first_value: # 개수가 맨처음과 다르다면
            decision = False # 존재하는 카드의 숫자종류의 개수가 다른 상황이므로 false. 즉 개수가 같냐 아니냐를 기준으로 판별
            break

    if decision is True: # 개수가 같은 상황. 즉 최대값과 개수를 출력
        max_key = list(count_num.keys())[0] # 딕셔너리에 첫번째 키값(숫자값) 을 max_key에 저장하기 위해 리스트로 형변환
        for key in count_num: # 딕셔너리의 숫자값들 조회
            if key > max_key: # 최대값 저장 과정
                max_key= key
        print(f"#{test_case} {max_key} {count_num[max_key]}") # 조건에 맞게 최대값과 그때의 숫자 개수를 출력
    else: # 개수가 다른 상황, 즉 개수가 제일 많은 수와 그때의 개수를 출력
        max_count = 0 # 개수저장 초기화
        max_key = 0
        for key in count_num: # 딕셔너리의 숫자값들 조회
            if count_num[key] > max_count: # 최대 개수 찾는 조건
                max_count = count_num[key]
                max_key = key # 최대 개수가 단일일 때는 그때의 값을 저장
            elif count_num[key] == max_count: # 개수가 같을때의 상황
                if key > max_key: # 숫자가 더크면
                    max_key = key # 그 수가 나오도록
        print(f"#{test_case} {max_key} {count_num[max_key]}")













