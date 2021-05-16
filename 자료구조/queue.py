# 큐 (Queue)
# 데이터를 임시 저장할 때 사용하는 자료구조이다.
# FIFO 정책을 따른다.

# 환형 큐 구현하기
class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.que = [None for _ in range(self.capacity)]
        self.front = 0
        self.rear = 0
        self.no = 0

    def is_empty(self):
        return self.no <= 0

    def is_full(self):
        return self.no >= self.capacity

    def enque(self, value):
        if self.is_full():
            raise IndexError
        self.que[self.rear] = value
        self.rear += 1
        self.no += 1

        if self.rear == self.capacity:
            self.rear = 0

    def deque(self):
        if self.is_empty():
            raise IndexError
        value = self.que[self.front]
        self.front += 1
        self.no -= 1

        if self.front == self.capacity:
            self.front = 0
        
        return value

# 링크드 큐 구현하기
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedQueue:
    def __init__(self, value):
        self.front = Node(value)
        self.rear = self.front

    def is_empty(self):
        return self.front is None

    def enque(self, value):
        self.rear.next = Node(value)
        self.rear = self.rear.next
        if self.is_empty():
            self.front = self.rear

    def deque(self):
        if self.is_empty():
            raise IndexError
        value = self.front.value
        self.front = self.front.next
        return value
