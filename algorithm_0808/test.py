# s = list('abc')
# print(s[1])
# s[1] = 'B'
# print(s)
# print(''.join(s))
# print(*s)

# N = int(input())
# text = [input() for _ in range(N)]
# # ['aaaaa', 'bbbbb']
# # text = [list(input()) for _ in range(N)]
# # [['a', 'a', 'a', 'a', 'a'], ['b', 'b', 'b', 'b', 'b']]
# cnt = 0
# for i in range(N):
#     for j in range(N):
#         if text[i][j] == '#': # ' ' 이 안에 뭘 찾고싶은지 넣으면 그 문자 또는 숫자를 찾음
#             cnt+=1
# print(cnt)

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1 , 1 + T):
    text = input()
    print(f'#{tc}',text[::-1])
