import sys
sys.stdin = open('input_3.txt')
T = int(input())
for tc in range(1, 1 + T):
    N = 5
    arr = [input() for _ in range(N)]
    new_arr =[]

    for j in range(15):
        for i in range(5):
            try:
                new_arr.append(arr[i][j])
            except:
                pass
    print(f'#{tc}',''.join(new_arr))
