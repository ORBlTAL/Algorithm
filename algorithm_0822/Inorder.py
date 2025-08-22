"""
배열 데이터에서 필요한 정보들을 뽑아와서 트리 데이터를 만들고, inorder 스캔 방식으로 출력
출력 번호에 맞게 딕셔너리 할당해서 의도한 문자대로 출력되게
"""


import sys
sys.stdin = open('input_3.txt')
T = 10

def calc(node_index):
    if len(tree_info[node_index]) == 2:
        return int(tree_info[node_index][1])
    else:
        left_child = int(tree_info[node_index][2])
        right_child = int(tree_info[node_index][3])

        char = tree_info[node_index][1]

for tc in range(1,T + 10):
    V = int(input())
    tree_info = [[] for _ in range(V+1)]
    for _ in range(V):
        node_input = input().split()
        tree_info[int(node_input[0])] = node_input

