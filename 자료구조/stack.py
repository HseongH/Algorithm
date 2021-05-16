# 스택 (Stack)
# 데이터를 임시 저장할 때 사용하는 자료구조이다.
# LIFO 정책을 따른다.

# 파이썬 제공 메서드로 구성하기
class Stack:
    def __init__(self):
        self.stk = []

    def is_empty(self):
        return len(self.stk) <= 0

    def push(self, value):
        self.stk.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError
        return self.stk.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError
        return self.stk[-1]

# 메서드 없이 구현하기
class CustomStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stk = [None for _ in range(self.capacity)]
        self.ptr = 0

    def is_empty(self):
        return self.ptr <= 0

    def is_full(self):
        return self.ptr >= self.capacity

    def push(self, value):
        if self.is_full():
            raise IndexError
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self):
        if self.is_empty():
            raise IndexError
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self):
        if self.is_empty():
            raise IndexError
        return self.stk[self.ptr - 1]
