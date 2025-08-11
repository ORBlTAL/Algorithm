import sys
sys.stdin = open('input_2.txt')
T = int(input())
for tc in range(1, 1+T):
    first = input()
    second = input()
    if first in second:
        print(f'#{tc}',1)
    else:
        print(f'#{tc}',0)
