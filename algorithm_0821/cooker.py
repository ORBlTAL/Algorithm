import sys
from itertools import permutations
sys.stdin = open('input_3.txt')
T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr= [list(map(int, input().split())) for _ in range(N)]