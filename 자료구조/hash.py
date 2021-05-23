# 해시 (Hash)
# 데이터 저장 공간에 키와 값의 형태로 데이터를 저장하는 자료구조
# 키(key)를 대입해 값을 찾아오기 때문에 탐색 속도가 매우 빠르다.

# 해시 충돌: 해시는 제한된 자료 공간 내에 키(key)를 특정 연산을 통해 해시 값으로 변환한 후 사용하는 데 이 과정에서 중복된 해시 값을 가지는 경우 충돌이 났다고 얘기한다.
#   해결 방법 1. chained hash: 충돌이 났을 때 같은 자료 공간 내에 링크드 리스트를 생성해 그 공간에 새로운 데이터를 저장한다.
#   방법 2. open addressing (개방 주소법): 충돌이 났을 때 자료 구조를 탐색하며 비어있는 공간에 새로운 데이터를 저장한다. (이때 저장 공간 내에는 데이터가 있는 경우, 비어 있는 경우, 데이터를 삭제한 경우 세 가지 상태를 나타내는 정보를 담고있어야 한다.)

# chained hash 구현
from hashlib import sha256

class Node:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

class ChainedHash:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None for _ in range(self.capacity)]

    def hash_value(self, key):
        if isinstance(key, int):
            return key % self.capacity
        return(int(sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

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

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
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
                print(f'    -> {p.key} ({p.value})', end=' ')
                p = p.next
            print()

# open addressing 구현
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

    def set_stat(self, stat):
        self.stat = stat

class OpenAddressing:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [Bucket() for _ in range(self.capacity)]

    def hash_value(self, key):
        if isinstance(key, int):
            return key % self.capacity
        return int(sha256(str(key).encode()).hexdigest(), 16) % self.capacity

    def rehash_value(self, key):
        return (self.hash_value(key) + 1) % self.capacity

    def search_node(self, key):
        hash = self.hash_value(key)
        p = self.table[hash]

        for _ in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.rehash_value(hash)
            p = self.table[hash]
        
        return None

    def search(self, key):
        p = self.search_node(key)

        if p:
            return p.value
        return None

    def add(self, key, value):
        if self.search_node(key):
            return False

        hash = self.hash_value(key)
        p = self.table[hash]

        for _ in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)
            p = self.table[hash]

        return False

    def remove(self, key):
        p = self.search_node(key)

        if p is None:
            return False
        p.set_stat(Status.DELETED)
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
