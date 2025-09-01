import sys
sys.stdin = open('input_2.txt')

T = int(input())
for tc in range(1, 1 + T) :
    N, M = map(str, input().split())
    M = int(M)
    arr = input().split()
    # sorted key 커스텀
    order = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN'] # 리스트를 이 순서대로 나열
    rank = {} # 키,값 할당을 통해 정렬하기위해 딕셔너리 선언
    i = 0 # 할당할 값
    for category in order: # zro부터 불러옴
        rank[category] = i # ZRO : 0 , ONE : 1 이런식으로 저장
        i +=1
    def sort_key(value): #
        if value in rank: #arr 배열로부터 받아온 값이 rank 딕셔너리에 있으면
            return  rank[value] # 그 값을 키로 넣어서 value를 리턴(ZRO 면0, ONE 이면 1
        else:
            return len(rank) # 그 이외 입력이 들어오면 길이를 반환

    sorted_arr = sorted(arr, key=sort_key) # 커스텀한 키로 sorted 메서드 적용
    print(f'#{tc}') # 형식에 맞게 출력하기 위해 print 2개 사용
    print(*sorted_arr) # 언패킹해서 출력