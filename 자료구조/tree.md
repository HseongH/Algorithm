# 트리 (Tree)

## 1. 트리 (Tree) 구조

- 트리: Node와 Branch를 이용해서 사이클을 이루지 않도록 구성한 데이터 구조
- 트리 중 이진 트리 (Binary Tree) 형태의 구조로, 탐색(검색) 알고리즘 구현을 위해 많이 사용된다.

***

## 2. 알아둘 용어

- Node: 트리에서 데이터를 저장하는 기본 요소 (데이터와 다른 연결된 노드에 대한 Branch 정보 포함)
- Root Node: 트리 맨 위에 있는 노드
- Level: 최상위 노드를 Level 0으로 하였을 때, 하위 Branch로 연결된 노드의 깊이를 나타냄
- Parent Node: 어떤 노드의 상위 레벨에 연결된 노드
- Child Node: 어떤 노드의 다음 레벨에 연결된 노드
- Leaf Node: Child Node가 하나도 없는 노드
- Sibling: 동일한 Parent Node를 가진 노드
- Depth: 트리에서 Node가 가질 수 있는 최대 Level

***

## 3. 이진 트리와 이진 탐색 트리 (Binary Search Tree)

- 이진 트리: 노드의 최대 Branch가 2인 트리
- 이진 탐색 트리 (Binary Search Tree, BST): 이진 트리에 다음과 같은 추가적인 조건이 있는 트리
    - 왼쪽 노드는 해당 노드보다 작은 값, 오른쪽 노드는 해당 노드보다 큰 값을 가지고 있음

***

## 4. 이진 탐색 트리의 장점과 주요 용도

- 주요 용도: 데이터 검색(탐색)
- 장점: 탐색 속도를 개선할 수 있음 (검색을 실행할 때마다 후보군을 반씩 줄여나갈 수 있음)

***

## 5. 코드로 구현하기

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, data):
        self.root = Node(data)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return True

        p = self.root

        while True:
            if data < p.data:
                if p.left is None:
                    p.left = Node(data)
                    return True
                p = p.left
            else:
                if p.right is None:
                    p.right = Node(data)
                    return True
                p = p.right

    def search(self, data):
        p = self.root

        while p:
            if data == p.data:
                return True
            elif data < p.data:
                p = p.left
            else:
                p = p.right

        return False

    def search_node(self, data):
        p = self.root
        parent_node = None

        while p:
            if data == p.data:
                break
            elif data < p.data:
                parent_node = p
                p = p.left
            else:
                parent_node = p
                p = p.right

        return p, parent_node
```

### 이진 탐색 트리 삭제

**case1. Leaf Node 삭제**

- Leaf Node: Child Node가 없는 Node
- 삭제할 Node의 Parent Node가 삭제할 Node를 가리키지 않도록 한다.

```python
def remove(self, data):
    p, parent_node = self.search_node(data)

    if parent_node is None:
        self.root = None
        return True
    elif p is None:
        return False

    if data < parent_node.data:
        parent_node.left = None
    else:
        parent_node.right = None

    del p
    return True
```

**case2. Child Node가 하나인 Node 삭제**

- 삭제할 Node의 Parent Node가 삭제할 Node의 Child Node를 가리키도록 한다.

```python
def remove(self, data):
    p, parent_node = self.search_node(data)

    if parent_node is None:
        self.root = None
        return True
    elif p is None:
        return False

    child_node = p.left or p.right

    if data < parent_node.data:
        parent_node.left = child_node
    else:
        parent_node.right = child_node

    del p
    return True
```

**case3. Child Node가 두 개인 Node 삭제**

1. 삭제할 Node의 오른쪽 자식 Node 중 가장 작은 자식 Node(가장 왼쪽에 위치한 Node)를 삭제할 Node 위치에 삽입
2. 삭제할 Node의 왼쪽 자식 Node 중 가장 큰 자식 Node(가장 오른쪽에 위치한 Node)를 삭제할 Node 위치에 삽입

**삭제 전략**

1. 삭제할 Node 위치에 대입할 Node 탐색
2. 탐색한 Node가 자식을 가지고 있다면
    - 오른쪽 자식의 가장 작은 Node를 탐색한 경우 탐색한 Node의 부모 Node 왼쪽이 탐색한 Node의 자식 요소를 가리키게 한다.
    - 왼쪽 자식의 가장 큰 Node를 탐색한 경우 탐색한 Node의 부모 Node 오른쪽이 탐색한 Node의 자식 요소를 가리키게 한다.
3. 삭제할 Node의 부모 Node가 탐색한 Node를 가리키게 한다.
4. 탐색한 Node의 왼쪽과 오른쪽이 각각 삭제할 Node의 왼쪽 Branch와 오른쪽 Branch를 가리키게 한다.

```python
# 왼쪽 자식 중 가장 큰 Node 탐색
def remove(self, data):
    p, parent_node = self.search_node(data)

    if parent_node is None:
        self.root = None
        return True
    elif p is None:
        return False

    change_parent = p
    change_node = p.left

    while change_node.right:
        change_parent = change_node
        change_node = change_node.right

    if change_parent != p:
        # 만약 while문을 한번도 수행하지 않았다면 위치를 바꿀 노드의 부모 노드가 현재 삭제할 노드이므로 그 노드에 탐색한 노드의 자식 노드를 연결한다면 탐색한 노드의 자식 노드로 이동할 방법이 없어진다. 또한 삭제할 노드의 왼쪽 노드가 탐색한 노드이므로 삭제할 노드의 왼쪽 노드를 탐색한 노드의 왼쪽에 연결한다면 탐색한 노드의 왼쪽 포인터는 자기 자신을 가리키게 된다. 따라서 이 구문은 while문이 적어도 한번 이상 수행되었을 때 수행되어야 한다.
        change_parent.right = change_node.left
        change_node.left = p.left

    change_node.right = p.right

    if data < parent_node.data:
        parent_node.left = change_node
    else:
        parent_node.right = change_node

    del p
    return True
```

```python
# 오른쪽 자식 중 가장 작은 노드 탐색
def remove(self, data):
    p, parent_node = self.search_node(data)

    if parent_node is None:
        self.root = None
        return True
    elif p is None:
        return False

    change_parent = p
    change_node = p.right

    while change_node.left:
        change_parent = change_node
        change_node = change_node.left

    if change_parent != p:
        change_parent.left = change_node.right
        change_node.right = p.right

    change_node.left = p.left

    if data < parent_node.data:
        parent_node.left = change_node
    else:
        parent_node.right = change_node

    del p
    return True
```

### 코드 종합하기

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, data):
        self.root = Node(data)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return True

        p = self.root

        while True:
            if data < p.data:
                if p.left is None:
                    p.left = Node(data)
                    return True
                p = p.left
            else:
                if p.right is None:
                    p.right = Node(data)
                    return True
                p = p.right
    
    def search(self, data):
        p = self.root

        while p:
            if data == p.data:
                return True
            elif data < p.data:
                p = p.left
            else:
                p = p.right

        return False

    def search_node(self, data):
        p = self.root
        parent_node = None

        while p:
            if data == p.data:
                break
            elif data < p.data:
                parent_node = p
                p = p.left
            else:
                parent_node = p
                p = p.right

        return p, parent_node

    def remove(self, data):
        p, parent_node = self.search_node(data)

        if parent_node is None:
            self.root = None
            return True
        elif p is None:
            return False

        if p.left is None and p.right is None:
            if data < parent_node.data:
                parent_node.left = None
            else:
                parent_node.right = None
        elif p.left and p.right:
            # 왼쪽 노드 중 가장 큰 노드 탐색
            change_parent = p
            change_node = p.left

            while change_node.right:
                change_parent = change_node
                change_node = change_node.right

            if change_parent != p:
                change_parent.right = change_node.left
                change_node.left = p.left

            change_node.right = p.right

            if data < parent_node.data:
                parent_node.left = change_node
            else:
                parent_node.right = change_node
        else:
            child_node = p.left or p.right

            if data < parent_node.data:
                parent_node.left = child_node
            else:
                parent_node.right = child_node

        del p
        return True
```
