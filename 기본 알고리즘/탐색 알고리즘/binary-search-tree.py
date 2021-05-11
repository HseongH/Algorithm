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
    def __init__(self, root) -> None:
        self.root = Node(root)
    
    def insert(self, value) -> bool:
        current_node = self.root

        while True:
            if value == current_node.value:
                break
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = Node(value)
                    return True
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = Node(value)
                    return True
                current_node = current_node.right

        return False

    def search(self, value) -> bool:
        current_node = self.root

        while current_node:
            if value == current_node.value:
                return True
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return False

    def search_node(self, value) -> Any:
        current_node = self.root
        parent_node = self.root

        while current_node:
            if value == current_node.value:
                return [current_node, parent_node]
            elif value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            else:
                parent_node = current_node
                current_node = current_node.right
        
        return [current_node, parent_node]

    def remove(self, value) -> bool:
        remove_node, parent_node = self.search_node(value)

        if remove_node is None:
            return False

        if remove_node.left is None and remove_node.right is None:
            if value < parent_node.value:
                parent_node.left = None
            else:
                parent_node.right = None
        elif remove_node.left and remove_node.right:
            child_parent = remove_node
            child_node = remove_node.left
            swap = False

            while child_node.right:
                child_parent = child_node
                child_node = child_node.right
                swap = True

            if swap:
                if child_node.left:
                    child_parent.right = child_node.left
                else:
                    child_parent.right = None
                child_node.left = remove_node.left

            if value < parent_node.value:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
                
            child_node.right = remove_node.right
        else:
            child_node = remove_node.left or remove_node.right

            if value < parent_node.value:
                parent_node.left = child_node
            else:
                parent_node.right = child_node

        del remove_node
        return True
