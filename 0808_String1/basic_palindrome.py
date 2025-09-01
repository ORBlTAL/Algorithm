import sys
sys.stdin = open('input_0.txt')
T = int(input())
for tc in range(1, 1 + T):
    text = input()
    if text == text[::-1]:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')