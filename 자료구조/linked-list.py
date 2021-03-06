# 링크드 리스트 (Linked List)
# 하나의 노드가 데이터를 저장하는 부분과 다음 노드의 위치를 가리키는 부분으로 구성되어 있음

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head

    def add(self, value):
        self.tail.next = Node(value)
        self.tail = self.tail.next

    def search(self, value):
        node = self.head

        while node.next:
            if node.next.value == value:
                return node
            node = node.next
        
        return None

    def insert(self, search, value):
        node = self.search(search)

        if node is None:
            return False

        node.next.next = Node(value, node.next.next)
        return True

    def delete(self, value):
        node = self.search(value)

        if node is None:
            return False

        node.next = node.next.next
        return True

    def desc(self):
        node = self.head

        while node:
            print(node.value)
            node = node.next
