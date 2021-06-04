# 스택 (Stack)

- 데이터를 제한적으로 접근할 수 있는 구조
- 한쪽 끝에서만 자료를 넣거나 뺄 수 있는 구조
- LIFO (Last In First Out) 정책을 따른다.
    - 가장 나중에 저장한 데이터를 가장 먼저 꺼낸다.

## 스택의 활용

- 재귀함수
- 웹 브라우저 뒤로가기 버튼

## 주요 기능

- push: 데이터를 스택에 넣기
- pop: 데이터를 스택에서 꺼내기
- peek: 가장 최근에 저장한 데이터를 조회한다.

## 스택의 장단점

- 장점
    - 구조가 단순해 구현이 쉽다.
    - 데이터를 저장 / 읽고 쓰는 데 속도가 빠르다.
- 단점
    - 미리 데이터 최대 갯수를 정해야 한다.
        - 파이썬의 경우 재귀 함수는 최대 1000번까지 호출이 가능하다.
    - 저장 공간의 낭비가 발생할 수 있다.
        - 미리 최대 갯수만큼 저장 공간을 확보해야 하기 때문

> 스택은 단순하고 빠른 성능을 위해 배열 구조로 주로 구현되는 데, 배열로 스택을 구현할 시 위와 같은 단점이 있을 수 있다.

## 코드로 구현하기

### 파이썬 기본 메서드(append, pop) 사용

```python
class Stack:
    def __init__(self):
        self.stk = list()

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
```

### 기본 메서드 없이 구현하기

```python
class Stack:
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
```
