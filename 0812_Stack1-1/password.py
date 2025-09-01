import sys
sys.stdin = open('input_4.txt')
T = 10
for tc in range(1, 1+T):
    N , arr = map(list,input().split()) # N은 필요없음
    i = 0 # 0 부터 시작
    while i < len(arr)-1: # i, i+1 의 연속된 인덱스를 조회해야함. 연속된 값이 없는 경우 인덱스 범위를 고려해 len(arr)-1 까지
        if arr[i] == arr[i+1]: # 연속된 2개가 같을경우
            arr.pop(i) # 지워버린다
            arr.pop(i) # 위에서 i번째가 지워져 i+1이 i 번째가 되므로
            if i > 0: # pop 하고 나서의 문자열이 다시 연속될 수 있으니
                i -= 1 # 다시 앞으로 가서 조사
        else: # 그게 아니면 +1 씩 해줘서 다음칸 조사
            i += 1
    print(f'#{tc}',''.join(arr)) # 문제 조건에 맞게 출력