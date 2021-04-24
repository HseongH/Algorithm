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
        parent_node = self.root

        while current_node is not None:
            if value == current_node.value:
                return [current_node, parent_node]
            elif value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            else:
                parent_node = current_node
                current_node = current_node.right

    def remove(self, value):
        current_node, parent_node = self.search_node(value)
                
        if current_node is None:
            return False

        if current_node.left is None and current_node.right is None:
            if value < parent_node.value:
                parent_node.left = None
            else:
                parent_node.right = None
        elif current_node.left and current_node.right:
            change_node_parent = current_node
            change_node = current_node.right

            if change_node.left:
                while change_node.left:
                    change_node_parent = change_node
                    change_node = change_node.left

                if change_node.right:
                    change_node_parent.left = change_node.right
                else:
                    change_node_parent.left = None
                change_node.right = current_node.right

            if value < parent_node.value:
                parent_node.left = change_node
            else:
                parent_node.right = change_node
                
            change_node.left = current_node.left
        else:
            child_node = current_node.left or current_node.right

            if value < parent_node.value:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
                
        del current_node
        return True
