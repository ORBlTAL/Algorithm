import sys
sys.stdin = open('input_4.txt')
T = 10
def calc(node_index):
    if len(tree[node_index]) == 2:
        return int(tree[node_index][1])
    else:
        left_child = int(tree[node_index][2])
        right_child = int(tree[node_index][3])

        left_val = calc(left_child)
        right_val = calc(right_child)

        op = tree[node_index][1]
        if op == '+':
            return left_val + right_val
        elif op == '-':
            return left_val - right_val
        elif op == '*':
            return left_val * right_val
        else:
            return left_val // right_val


for tc in range(1, 1+T):
    V = int(input())
    tree = [[] for _ in range(V+1)]
    for _ in range(V):
        node_input = input().split()
        tree[int(node_input[0])] = node_input
    result = calc(1)
    print(f'#{tc}', result)