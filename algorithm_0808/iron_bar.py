import sys
sys.stdin = open('input_4.txt')
T = int(input())
for tc in range(1, 1 + T):
    laser = list(input())
    # print(laser)
    # print(len(laser))
    first_shape = laser[0]
    last_shape = laser[len(laser) - 1]
    cnt = 0
    for i in range(len(laser)-1):
        if laser[i] == first_shape and laser[i+1] == last_shape:
            cnt+=1
    print(cnt)
