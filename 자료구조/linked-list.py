# 링크드 리스트 (Linked List)
# 하나의 노드가 데이터를 저장하는 부분과 다음 노드의 위치를 가리키는 부분으로 구성되어 있음

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        node = self.head

        while node.next:
            if node.data == data:
                return False
            node = node.next
        
        node.next = Node(data)
        return True

    def search(self, data):
        node = self.head
        idx = 0

        while node:
            if node.data == data:
                return idx
            node = node.next
            idx += 1
        
        return -1

    def remove(self, data):
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
            return True
        else:
            node = self.head

            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    
                    return True
                node = node.next

            return False
