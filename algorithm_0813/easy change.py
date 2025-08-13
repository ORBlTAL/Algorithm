import sys
sys.stdin = open('input_2.txt')
T = int(input())
for tc in range(1, 1 + T):
    money = int(input())
    a = b = c = d = e = f = g = h = 0 # 5만원 부터 10원까지의 개수를 저장할 변수들 선언
    while money >= 10: # while이 10 이상일 때
        if money // 50000 >= 1: # 돈을 나눴을때 몫이 1 이상이면
            a = money // 50000 # 몫만큼의 필요한 5만원권의 개수 이므로 a에 할당
            money = money % 50000 # 그 이후는 5만원을 나눈 나머지를 계산해야하니 나머지를 구함

        elif money // 10000 >= 1:   # 원리는 맨처음 if문과 동일
            b = money // 10000
            money = money % 10000

        elif money // 5000 >= 1:
            c = money // 5000
            money = money % 5000

        elif money // 1000 >= 1:
            d = money // 1000
            money = money % 1000

        elif money // 500 >= 1:
            e = money // 500
            money = money % 500

        elif money // 100 >= 1:
            f = money // 100
            money = money % 100

        elif money // 50 >= 1:
            g = money // 50
            money = money % 50

        elif money // 10 >= 1:
            h = money // 10
            money = money % 10
    print(f'#{tc}')
    print(a,b,c,d,e,f,g,h)
