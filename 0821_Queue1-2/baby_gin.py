"""
- 0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우를 run이라 하고, 3장의 카드가 동일한 번호를 갖는 경우를 triplet이라 한다.

- 그리고, 6장의 카드가 run과 triplet로만 구성된 경우를 baby-gin으로 부른다.

- 6자리의 숫자를 입력 받아 baby-gin 여부를 판단하라.



[입력 예]

- 667767은 두 개의 triplet이므로 baby-gin이다. (666, 777)

- 054060은 한 개의 run과 한 개의 triplet이므로 역시 baby-gin이다.(456, 000)

- 101123은 한 개의 triplet이 존재하나, 023이 run이 아니므로 baby-gin이 아니다. (123을 run으로 사용하더라도  011이 run이나 triplet이 아님)
"""

import sys
from itertools import combinations

def run(card):
    return card[0] + 2 == card[1] + 1 == card[2] # run 조건이 참일 때 리턴

def triplet(card):
    return card[0] == card[1] == card[2] # triplet 조건이 참일 때 리턴

def baby_gin_comb(card):
    for group in combinations(range(6),3): # 6개 중에서 3개를 뽑아 조합으로
        g1 = []
        for idx in group: # 위에서 뽑은 조합 요소를 토대로 g1 리스트에 3개씩 저장
            g1.append(card[idx])

        g2 = []
        for i in range(6): # 위의 그룹에 속하지 않는 카드들끼리 뽑아서 g2 리스트에 저장
            if i not in group:
                g2.append(card[i])

        ok1 = run(g1) or triplet(g1) # g1이 run 또는 triplet일 떄
        ok2 = run(g2) or triplet(g2) # g2가 run 또는 tripelt 일 때
        if ok1 and ok2: # 둘 다 둘 중 하나는 충족하고 있어야 만족한다.
            return True
    return False

sys.stdin = open('input_1.txt')
T = int(input())
for tc in range(1, 1 + T):
    card = list(map(int,input()))
    card.sort() # 정렬

    if baby_gin_comb(card): # 함수에 넣어서 나온 결과가 참이냐 거짓이냐에 따라 분류
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)