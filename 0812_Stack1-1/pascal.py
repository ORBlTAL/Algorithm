import sys
import math # math 라이브러리 사용
sys.stdin = open('input_3.txt')
T = int(input())
for tc in range(1, 1 + T):
    N = int(input())

    triangle = [] # 파스칼의 삼각형을 저장할 배열 선언
    for i in range(N):
        row = [] # 2차원 이므로 row 리스트 추가
        for j in range(i + 1):  # 순열공식에 의거 계산
            val = math.factorial(i) // (math.factorial(i - j) * math.factorial(j))
            row.append(val) # 계산된 결과를 row행에 추가
        triangle.append(row) # row행 전체를 triangle 리스트에 추가
    print(f'#{tc}')
    for row in triangle: # 한 행씩 언패킹 해서 출력
        print(*row)
