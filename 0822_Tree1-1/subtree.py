"""
N값으로 지정된 노드의 자기 자신을 포함해 그 밑에 몇개의 노드가 연관되어 있는지 개수를 세면 된다.
"""
# import sys
# sys.stdin = open('input_2.txt')
# T = int(input())
# def preorder(node):
#     if node == 0:               # 노드가 0이면
#         return []               # 빈 리스트 반환
#     result = [node]             # 현재 노드를 리스트에 담음
#     result += preorder(left[node])   # 왼쪽 서브트리 결과와 합침
#     result += preorder(right[node])  # 오른쪽 서브트리 결과와 합침
#     return result               # 전체 리스트 반환
#
#
# for tc in range(1, 1 + T):
#     E , root = map(int, input().split())
#     edge = list(map(int, input().split()))
#
#     left = [0] * (E+2) # E+1 이 V 이므로
#     right = [0] * (E+2)
#     for i in range(E):
#         parent , child = edge[i*2] , edge[i*2+1] # 부모와 자녀 분리
#         if left[parent] == 0:
#             left[parent] = child # left, right 리스트에 왼쪽, 오른쪽 노드 나눠서 저장
#         else:
#             right[parent] = child
#     print(f'#{tc}', len(preorder(root)))

import sys

sys.stdin = open('input_3.txt')

# 중위 순회
def inorder(node_index):
    # 자식이 없는 경우(리프 노드) 그냥 자기 알파벳만 출력
    if len(tree_info[node_index]) == 2:
        return tree_info[node_index][1]

    # 왼쪽, 자기 자신, 오른쪽 순서로 이어붙임 / 길이를 토대로 왼쪽 자식이 있는지, 오른쪽도 있는지 구분
    result = ""
    if len(tree_info[node_index]) >= 3:   # 왼쪽 자식이 있는 경우
        result += inorder(int(tree_info[node_index][2])) # 먼저 재귀 호출
    result += tree_info[node_index][1]    # 자기 자신
    if len(tree_info[node_index]) == 4:   # 오른쪽 자식이 있는 경우
        result += inorder(int(tree_info[node_index][3])) # 재귀 호출
    return result


T = 10
for tc in range(1, T + 1):
    N = int(input())  # 노드의 총 수
    tree_info = [[] for _ in range(N + 1)]

    for _ in range(N):
        node_input = input().split()
        tree_info[int(node_input[0])] = node_input # 노드 번호를 인덱스로 사용하여 정보 저장

    result = inorder(1)
    print(f"#{tc} {result}")
