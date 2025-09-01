import sys
sys.stdin = open('input_1.txt')
T = int(input())

for tc in range(1, 1 + T):
    # str1 , str2 모두 리스트로 받아옴
    N = list(input())
    M = list(input())

    new_dict = {} # 딕셔너리 선언
    for i in range(len(N)):
        new_dict[N[i]] = 0 # 각 문자열을 key로 선언, 값은 모두 0. 중복되는 것도 없엠
    new_list_key = list(new_dict.keys()) # key 값들만 따로 선언
    for i in range(len(M)): # M str을 순회
        for j in range(len(new_list_key)): # M과 new_list의 key값들과 비교 예정
            if M[i] == new_list_key[j]: # 서로 같은 문자일 경우
                new_dict[new_list_key[j]] += 1 # new_dict의 value 값들에 +1 씩
    new_list_value = list(new_dict.values()) # value로 이루어진 새 리스트 선언

    print(f'#{tc}',max(new_list_value)) # value 리스트에서 max로 최대값 뽑음.