"""
visited 생성
큐생성, 시작점 인큐
인큐표시
반복
    디큐
    방문해서 할 일
    방문정점에 인접하고 미방문이면
        인큐.... '벽이 아니고' 로 풀이 ('통로면' 으로 풀면 문제 발생)
         ㄴ visited[ni][nj] == 0
        인큐표시
"""
# def find_start(N):
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 2:
#                 return i, j
#
# def bfs(i, j, N):
#     visited =[[0] * N for _ in range(N)]
#     q = [[i,j]]
#     visited[i][j] = 1
#     while q:
#         ti, tj = q.pop(0)
#         if maze[ti][tj] == 3:
#             return visited[ti][tj] - 2
#         for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
#             wi, wj = ti + di, tj + dj
#             if 0 <= wi < N and 0 <= wj < N and maze[wi][wj]!=1 and visited[wi][wj]:
#                 q.append([wi,wj])
#                 visited[wi][wj] = visited[ti][tj] + 1
#
# N = int(input())
# maze = [list(map(int, input())) for _ in range(N)]
# sti , stj = find_start(N)
# ans = bfs(sti, stj, N)
# print(ans)

# for i in range(1,4):
#     for j in range(1,4):
#         if i != j:
#             for k in range(1,4):
#                 if i != k and j != k:
#                     print(i,j,k)

# def perm(selected, remaining):
#     if not remaining:
#         print(selected)
#         return
#
#     for i in range(len(remaining)):
#
#         pick = remaining[i]
#
#         new_remaining = remaining[:i] + remaining[i + 1 : ]
#
#         perm(selected + [pick], new_remaining)
#
# perm([] , [1,2,3])

# numbers = [1,2,3,4]
# n = len(numbers)
#
# for i in range(n):
#     for j in range(1+i , n):
#         for k in range(1 + j, n):
#             print(numbers[i] , numbers[j], numbers[k])

# def comb(arr,r):
#     result = []
#     if r == 0:
#         return [[]]
#
#     for i in range(len(arr)):
#         elem = arr[i]
#
#         for rest in comb(arr[i+1 :], r-1):
#             result.append([elem] + rest)
#
#     return result
#
# all_combs = comb([1,2,3,4] , 3)
# print(all_combs)


from itertools import combinations

arr = list(range(1,11)) # 1부터 10 까지 리스트 생성
N = len(arr)

new_arr = [] # 모두 합쳐서 10이되는 조합일 경우에만 여기 리스트에 저장
for i in range(1, N + 1):
    for j in combinations(arr,i): # 1~10 크기의 조합을 다 찾음
        if sum(j) == 10: # 해당 길이의 조합에서의 합이 10일 때
            new_arr.append(j) # new_arr에 저장
new_arr.sort() # 정렬

for k in new_arr: # 언패킹해서 출력
    print(*k)





























