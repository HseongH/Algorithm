class MaxHeap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)
        
    def swap_up(self, idx):
        if idx <= 1:
            return False
        
        parent_idx = idx // 2
        
        if self.heap_array[idx] > self.heap_array[parent_idx]:
            return True
        return False
    
    def insert(self, data):
        if len(self.heap_array) <= 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        
        self.heap_array.append(data)
        idx = len(self.heap_array) - 1
        
        while self.swap_up(idx):
            parent_idx = idx // 2
            self.heap_array[parent_idx], self.heap_array[idx] = self.heap_array[idx], self.heap_array[parent_idx]
            idx = parent_idx
            
        return True
    
    def swap_down(self, parent_idx):
        left_idx = parent_idx * 2
        right_idx = parent_idx * 2 + 1
        
        if len(self.heap_array) <= left_idx:
            return False
        elif len(self.heap_array) <= right_idx:
            if self.heap_array[parent_idx] < self.heap_array[left_idx]:
                return True
            return False
        else:
            child_value = self.heap_array[left_idx] if self.heap_array[left_idx] > self.heap_array[right_idx] else self.heap_array[right_idx]
        
            if self.heap_array[parent_idx] < child_value:
                return True
            return False
        
    def remove(self):
        if len(self.heap_array) <= 1:
            return None
        
        max = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        self.heap_array.pop()
        
        parent_idx = 1
        
        while self.swap_down(parent_idx):
            left_idx = parent_idx * 2
            right_idx = parent_idx * 2 + 1
            
            if len(self.heap_array) <= right_idx:
                self.heap_array[parent_idx], self.heap_array[left_idx] = self.heap_array[left_idx], self.heap_array[parent_idx]
                parent_idx = left_idx
            else:
                child_idx = left_idx if self.heap_array[left_idx] > self.heap_array[right_idx] else right_idx
                self.heap_array[parent_idx], self.heap_array[child_idx] = self.heap_array[child_idx], self.heap_array[parent_idx]
                parent_idx = child_idx
                
        return max

class MinHeap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)
        
    def swap_up(self, idx):
        if idx <= 1:
            return False
        
        parent_idx = idx // 2
        
        if self.heap_array[idx] < self.heap_array[parent_idx]:
            return True
        return False
    
    def insert(self, data):
        if len(self.heap_array) <= 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        
        self.heap_array.append(data)
        idx = len(self.heap_array) - 1
        
        while self.swap_up(idx):
            parent_idx = idx // 2
            self.heap_array[parent_idx], self.heap_array[idx] = self.heap_array[idx], self.heap_array[parent_idx]
            idx = parent_idx
            
        return True
    
    def swap_down(self, parent_idx):
        left_idx = parent_idx * 2
        right_idx = parent_idx * 2 + 1
        
        if len(self.heap_array) <= left_idx:
            return False
        elif len(self.heap_array) <= right_idx:
            if self.heap_array[parent_idx] > self.heap_array[left_idx]:
                return True
            return False
        else:
            child_value = self.heap_array[left_idx] if self.heap_array[left_idx] < self.heap_array[right_idx] else self.heap_array[right_idx]
        
            if self.heap_array[parent_idx] > child_value:
                return True
            return False
        
    def remove(self):
        if len(self.heap_array) <= 1:
            return None
        
        min = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        self.heap_array.pop()
        
        parent_idx = 1
        
        while self.swap_down(parent_idx):
            left_idx = parent_idx * 2
            right_idx = parent_idx * 2 + 1
            
            if len(self.heap_array) <= right_idx:
                self.heap_array[parent_idx], self.heap_array[left_idx] = self.heap_array[left_idx], self.heap_array[parent_idx]
                parent_idx = left_idx
            else:
                child_idx = left_idx if self.heap_array[left_idx] < self.heap_array[right_idx] else right_idx
                self.heap_array[parent_idx], self.heap_array[child_idx] = self.heap_array[child_idx], self.heap_array[parent_idx]
                parent_idx = child_idx
                
        return min