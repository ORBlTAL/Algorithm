import itertools
arr = list(range(1, 11)) # 1~10까지 조합중에서 해당 개수만큼 더했을 때 10이 되는 경우만 정리
fourth = list(itertools.combinations(arr, 4))
third = list(itertools.combinations(arr, 3))
second = list(itertools.combinations(arr, 2))
first = list(itertools.combinations(arr, 1))

def four(list_4): # 조합의 합이 10이 되는 경우 반환
    for i in list_4:
        if sum(i) == 10:
            return i

def three(list_3): # 여러개의 경우 리스트에 저장
    new = []
    for i in list_3:
        if sum(i) == 10:
            new.append(i)
    return new

def two(list_2):
    new = []
    for i in list_2:
        if sum(i) == 10:
            new.append(i)
    return new

def one(list_1):
    new = []
    for i in list_1:
        if sum(i) == 10:
            new.append(i)
    return new


print(*four(fourth)) # 출력

for item in three(third): # 리스트의 요소 1개씩 선택한다음 튜플을 언패킹해서 출력
    print(*item)

for item in two(second):
    print(*item)

for item in one(first):
    print(*item)














