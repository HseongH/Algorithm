# 링크드 리스트 (Linked List)

- 데이터를 저장하기 위한 자료구조
- 배열은 순차적으로 연결된 공간에 데이터를 나열하는 자료구조
- 링크드 리스트는 떨어진 곳에 존재하는 데이터를 서로 연결해서 관리하는 자료구조

***

## 알아둘 용어

- 노드: 데이터 저장 단위 데이터 값, 포인터로 구성
- 포인터: 이전이나 다음 노드와의 연결 정보를 담고있다.

## 링크드 리스트의 장단점

- 장점
    - 미리 데이터 공간을 할당하지 않아도 된다.
- 단점
    - 연결을 위한 별도 데이터 공간이 필요하므로 저장공간 효율이 높지 않다.
    - 연결 정보를 찾는 시간이 필요하므로 접근 속도가 느리다.
    - 중간 데이터 삭제 시 데이터의 연결을 재구성하는 작업이 필요하다.

## 코드로 구현하기

```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def get_node(self, index):
        node = self.head

        for _ in range(index):
            if node is None:
                return None
            node = node.next

        return node

    def add(self, data):
        node = self.head

        while node.next:
            node = node.next

        node.next = Node(data)

    def insert(self, index, data):
        if index <= 0:
            new_node = Node(data, self.head)
            self.head = new_node
            return 

        node = self.get_node(index - 1)

        if node is None:
            return False
            
        node.next = Node(data, node.next)

    def delete(self, index):
        if index <= 0:
            self.head = self.head.next
            return

        node = self.get_node(index - 1)

        if node is None:
            return False

        node.next = node.next.next

    def desc(self):
        node = self.head

        while node:
            print(node.data)
            node = node.next
```
