# 해쉬 테이블 (Hash Table)

## 1. 해쉬 구조
- Hash Table: 키(Key)에 데이터(Value)를 저장하는 데이터 구조
    - Key를 통해 바로 데이터를 받아올 수 있으므로, 속도가 획기적으로 빨라짐
    - 파이썬 딕셔너리(Dictionary) 타입이 해쉬 테이블의 예(Key를 가지고 바로 데이터(Value)를 꺼냄)
    - 보통 배열로 미리 Hash Table 사이즈만큼 생성 후에 사용 (공간과 탐색 시간을 맞바꾸는 기법)     

***

## 2. 알아둘 용어
- 해쉬(Hash): 임의 값을 고정 길이로 변환하는 것
- 해쉬 테이블(Hash Table): 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조
- 해싱 함수(Hashing Function): Key에 대해 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수
- 해쉬 값(Hash Value) 또는 해쉬 주소(Hash Address): Key를 해싱 함수로 연산해서, 해쉬 값을 알아내고, 이를 기반으로 해쉬 테이블에서 해당 Key에 대한 데이터 위치를 일관성있게 찾을 수 있음
- 슬롯(Slot): 한 개의 데이터를 저장할 수 있는 공간
- 저장할 데이터에 대해 Key를 추출할 수 있는 별도 함수도 존재할 수 있음

***

## 3. 해쉬 테이블의 장단점과 주요 용도
- 장점
    - 데이터 저장/읽기 속도가 빠르다.(검색 속도가 빠르다.)
    - 해쉬는 키에 대한 데이터가 있는지(중복) 확인이 쉬움
- 단점
    - 일반적으로 저장공간이 좀 더 많이 필요하다.
    - **여러 키에 해당하는 주소가 동일할 경우 충돌을 해결하기 위한 별도 자료구조가 필요하다**
- 주요 용도
    - 검색이 많이 필요한 경우
    - 저장, 삭제, 읽기가 빈번한 경우
    - 캐쉬 구현시 (중복 확인이 쉽기 때문)

***

## 4. 충돌(Collision) 해결 알고리즘

### 4.1 Chaining 기법
- **개방 해슁 또는 Open Hashing 기법** 중 하나: 해쉬 테이블 저장공간 외의 공간을 활용하는 기법
- 충돌이 일어나면 링크드 리스트라는 자료 구조를 사용해서, 링크드 리스트로 데이터를 추가로 뒤에 연결시켜서 저장하는 기법

### 4.2 Linear Probing 기법
- **폐쇄 해슁 또는 Close Hasing 기법** 중 하나: 해쉬 테이블 저장공간 안에서 충돌 문제를 해결하는 기법
- 충돌이 일어나면, 해당 hash address의 다음 address부터 맨 처음 나오는 빈 공간에 저장하는 기법
    - 저장공간 활용도를 높이기 위한 기법

***

## 5. 코드로 구현

### 5.1 Chainig Hash 구현

```python
from hashlib import sha256

class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

class ChainedHash:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key):
        if isinstance(key, int):
            return key % self.capacity
        return(int(sha256(str(key).encode()).hexdigest, 16) % self.capacity)

    def search(self, key):
        hash = self.hash_value(key)
        p = self.table[hash]

        while p:
            if p.key == key:
                return p.value
            p = p.next

        return None

    def add(self, key, value):
        hash = self.hash_value(key)
        p = self.table[hash]

        while p:
            if p.key == key:
                return False
            p = p.next

        self.table[hash] = Node(key, value, self.table[hash])
        return True

    def remove(self, key):
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        while p:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            pp = p
            p = p.next

        return False

    def dump(self):
        for i in range(self.capacity):
            p = self.table[i]

            print(i, end=' ')

            while p:
                print(f'   -> {p.key} ({p.value})', end=' ')
                p = p.next
            print()
```

### 5.2 Linear Probing 구현

```python
from hashlib import sha256
from enum import Enum

class Status(Enum):
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2

class Bucket:
    def __init__(self, key=None, value=None, stat=Status.EMPTY):
        self.key = key
        self.value = value
        self.stat = stat

    def set_status(self, stat):
        self.stat = stat

class OpenAddressing:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [Bucket()] * self.capacity

    def hash_value(self, key):
        if isinstance(key, int):
            return key % self.capacity
        return(int(sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def rehash_value(self, key):
        return (self.hash_value(key) + 1) % self.capacity

    def search_node(self, key):
        hash = self.hash_value(key)
        p = self.table[hash]

        for _ in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.rehash_value(hash)
            p = self.table[hash]

        return None

    def search(self, key):
        p = self.search_node(key)

        if p is None:
            return False
        return p.value

    def add(self, key, value):
        if self.search_node(key):
            return False

        hash = self.hash_value(key)
        p = self.table[hash]

        for _ in range(self.capacity):
            if p.stat == Status.EMPY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)
            p = self.table[hash]

        return False

    def remove(self, key):
        p = self.search_node(key)

        if p is None:
            return False
        
        p.set_status(Status.DELETED)
        return True

    def dump(self):
        for i in range(self.capacity):
            p = self.table[i]

            print(f'{i:2}', end=' ')

            if p.stat == Status.OCCUPIED:
                print(f'{p.key} ({p.value})')
            elif p.stat == Status.EMPTY:
                print('--미등록--')
            elif p.stat == Status.DELETED:
                print('--삭제 완료--')
```
