# 이진 탐색 트리(Binary Search Tree)
# 이진 트리: 노드의 최대 Branch가 2인 트리
# 이진 탐색 트리: 이진 트리 중에서 가장 많이 사용되는 형태로 각 노드와 비교해 그 보다 작으면 왼쪽, 크면 오른쪽에 하위 노드를 정렬한다.
from typing import Any

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinSearchTree:
    def __init__(self, value) -> None:
        self.root = Node(value)

    def insert(self, value) -> bool:
        p = self.root

        while True:
            if value == p.value:
                return False
            if value < p.value:
                if p.left is None:
                    p.left = Node(value)
                    return True
                p = p.left
            else:
                if p.right is None:
                    p.right = Node(value)
                    return True
                p = p.right

    def search(self, value) -> bool:
        p = self.root

        while p:
            if value == p.value:
                return True
            elif value < p.value:
                p = p.left
            else:
                p = p.right
        
        return False
    
    def search_node(self, value) -> Any:
        parent_node = self.root
        p = self.root

        while p:
            if value == p.value:
                break
            elif value <= p.value:
                parent_node = p
                p = p.left
            else:
                parent_node = p
                p = p.right

        return [p, parent_node]

    def remove(self, value) -> bool:
        p, parent_node = self.search_node(value)

        if p is None:
            return False

        if p.left is None and p.right is None:
            if value < parent_node.value:
                parent_node.left = None
            else:
                parent_node.right = None
        elif p.left and p.right:
            change_parent = p
            change_node = p.right
            execution = False

            while change_node.left:
                change_parent = change_node
                change_node = change_node.left
                execution = True
            
            if execution:
                if change_node.right:
                    change_parent.left = change_node.right
                else:
                    change_parent.left = None
                change_node.right = p.right

            if value < parent_node.value:
                parent_node.left = change_node
            else:
                parent_node.right = change_node
                
            change_node.left = p.left
        else:
            child_node = p.left or p.right

            if value < parent_node.value:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
        
        del p
        return True
