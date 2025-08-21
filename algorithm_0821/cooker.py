import sys
from itertools import permutations
sys.stdin = open('input_3.txt')
T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr= [list(map(int, input().split())) for _ in range(N)]
"""
    순열로 풀꺼면 4개중 2개를 골라서 기존 순서, 반전된 순서 둘 다 더해줘야 A , B가 나온다.
     A가 2개 고르고, B 는 A가 안고른 2개를 배정 
     baby_gin 참고 
"""