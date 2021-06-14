# 큐 (Queue)

- 스택과 같이 데이터를 임시 저장할 목적으로 사용된다.
- 스택과는 반대로 FIFO(First In First Out) 정책을 따른다.
    - 가장 먼저 넣은 데이터를 가장 먼저 꺼내는 정책
- 줄을 서는 행위와 유사하다고 생각하면 된다.

***

## 알아둘 용어

- Enqueue: 큐에 데이터를 넣는 기능
- Dequeue: 큐에서 데이터를 꺼내는 기능
- Front: 큐에서 데이터를 꺼내는 부분을 가리킨다. (데이터가 저장되어 있는 가장 앞 부분을 가리킨다.)
- Rear: 큐에서 데이터를 저장하는 부분을 가리킨다. (큐의 맨 끝을 가리킨다. 데이터의 맨 끝과는 다르다.)

***

## 큐의 종류

### 1. 선형 큐

- 막대 모양으로 된 큐이다.
- 크기가 제한적이고, 빈 공간을 사용하기 위해선 데이터를 dequeue 하게 되면 모든 데이터를 한 칸씩 앞으로 옮겨야 한다.

### 2. 환형 큐

- 선형 큐의 단점을 보완한 큐이다.
- 데이터를 dequeue 해도 데이터를 한 칸씩 이동시키지 않고 front의 위치를 한 칸씩 뒤로 이동시켜 front가 맨 뒤에 닿으면 다시 0번부터 데이터를 접근하도록 한다.

### 3. 링크드 큐

- 링크드 리스트의 형태를 이용한 큐이다.
- 저장 공간에 제약이 없다는 장점이 있다.

***

## 코드로 구현하기

### 환형 큐 구현하기

```python
class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.que = [None] * self.capacity
        self.front = 0
        self.rear = 0
        self.no = 0

    def is_empty(self):
        return self.no <= 0

    def is_full(self):
        return self.no >= self.capacity

    def enqueue(self, value):
        if self.is_full():
            return False
        self.que[self.rear] = value
        self.rear += 1
        self.no += 1

        if self.rear >= self.capacity:
            self.rear = 0

    def dequeue(self):
        if self.is_empty():
            return False
        value = self.que[self.front]
        self.front += 1
        self.no -= 1

        if self.front >= self.capacity:
            self.front = 0

        return value
```

### 링크드 큐 구현하기

```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty():
        return self.head is None

    def enqueue(self, data):
        node = Node(data)

        if self.is_empty():
            self.tail = node
            self.head = self.tail
            return

        self.tail.next = node
        self.tail = self.tail.next

    def dequeue(self):
        if self.is_empty():
            return False

        node = self.head
        self.head = self.head.next
        return node.data
```
