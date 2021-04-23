class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt:
    def __init__(self, root):
        self.root = root
        
    def insert(self, value):
        current_node = self.root
        
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = Node(value)
                    break
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = Node(value)
                    break
                current_node = current_node.right
                
    def search(self, value):
        current_node = self.root
        
        while current_node:
            if value == current_node.value:
                return True
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False
    
    def search_node(self, value):
        current_node = self.root
        
        while current_node:
            if value < current_node.value:
                if current_node.left is None:
                    return [current_node, None]
                if value == current_node.left.value:
                    return [current_node, current_node.left]
                current_node = current_node.left
            else:
                if current_node.right is None:
                    return [current_node, None]
                if value == current_node.right.value:
                    return [current_node, current_node.right]
                current_node = current_node.right
    
    def remove(self, value):
        parent_node, remove_node = self.search_node(value)
        
        if remove_node is None:
            return False
        
        if remove_node.left is None and remove_node.right is None:
            if value < parent_node.value:
                parent_node.left = None
            else:
                parent_node.right = None
                
            del remove_node
            return True
        elif remove_node.left and remove_node.right:
            child_parent = remove_node
            child_node = remove_node.right
            
            while child_node.left:
                child_parent = child_node
                child_node = child_node.left
            
            if child_node.right:
                child_parent.left = child_node.right
            if value < parent_node.value:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
                
            child_node.left = remove_node.left
            child_node.right = remove_node.right
            del remove_node
            return True
        else:
            child_node = remove_node.left or remove_node.right
            
            if value < parent_node.value:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
                
            del remove_node
            return True
