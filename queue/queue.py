# class Queue:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.table = [None for _ in range(capacity)]
#         self.rear = 0
#         self.front = 0
#         self.no = 0

#     def is_empty(self):
#         return self.no <= 0
    
#     def is_full(self):
#         return self.no >= self.capacity

#     def enqueue(self, data):
#         if self.is_full():
#             return False
#         self.table[self.rear] = data
#         self.rear += 1
#         self.no += 1
#         if self.rear == self.capacity:
#             self.rear = 0

#     def dequeue(self):
#         if self.is_empty():
#             return False
#         data = self.table[self.front]
#         self.front += 1
#         self.no -= 1
#         if self.front == self.capacity:
#             self.front = 0
#         return data

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self, data):
        self.front = Node(data)
        self.rear = self.front
    
    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        self.rear.next = Node(data)
        self.rear = self.rear.next
        if self.is_empty():
            self.front = self.rear

    def dequeue(self):
        if self.is_empty():
            return False
        data = self.front.data
        self.front = self.front.next
        return data
