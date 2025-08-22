import sys
sys.stdin = open('input_1.txt')

def preorder(node): # 전위 순회
    if node !=0:
        print(node, end = ' ') # 처음 node는 루트 값이니 출력
        preorder(left[node]) # 좌측노드로 이동, V에 해당하는 값들 출력
        preorder(right[node]) # 이동할 좌측 노드가 없으면 우측 노드로 이동

def inorder(node): # 중위 순회
    if node !=0:
        inorder(left[node]) # 좌측 노드로 먼저 이동
        print(node, end=' ') # L에 해당하는 노드 출력
        inorder(right[node]) # 좌측 노드가 없으면 우측으로

def postorder(node): # 후위 순회
    if node !=0:
        postorder(left[node])
        postorder(right[node])
        print(node, end=' ')

V = int(input())
connector = V - 1

edge = list(map(int , input().split()))
left = [0] * (V + 1)
right = [0] * (V + 1)

for i in range(connector): # 간선의 크기 만큼
    parent, child = edge[i*2] , edge[i*2+1] # 노드중에서 부모와 자식을 분리

    if left[parent] == 0: # 좌측 노드부터 구함. 비어있으면 넣어줌
        left[parent] = child
    else:
        right[parent] = child # 좌측 노드가 차있을 경우에 읽어온 child 값은 우측 노드값 이므로 우측 노드에 할당

preorder(1)
print()
inorder(1)
print()
postorder(1)