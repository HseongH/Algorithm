class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None for _ in range(capacity)]
        self.ptr = 0

    def is_empty(self):
        return self.ptr <= 0

    def is_full(self):
        return self.ptr >= self.capacity
    
    def push(self, data):
        if self.is_full():
            return False
        self.table[self.ptr] = data
        self.ptr += 1

    def pop(self):
        if self.is_empty():
            return False
        self.ptr -= 1
        return self.table[self.ptr]

    def peek(self):
        if self.is_empty():
            return False
        return self.table[self.ptr - 1]
