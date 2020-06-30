class max_heap():
    def __init__(self,arr):
        self.arr = arr
        self.heap_size = len(arr)
        self.heap_length = len(arr)
        
    def max_heapify(self, i):
        left = 2*i
        right = 2*i + 1
        largest = i
        
        if left <= self.heap_size:
            if self.arr[left - 1] > self.arr[largest -1]:
                largest = left
        if right <= self.heap_size:
            if self.arr[right - 1] > self.arr[largest - 1]:
                largest = right
        if largest != i:
            tmp = self.arr[i-1]
            self.arr[i-1] = self.arr[largest-1]
            self.arr[largest -1] = tmp
            self.max_heapify(largest)
    
    def build_max_heap(self):
        nonleaf = int(self.heap_size/2)
        for i in range(nonleaf, 0, -1):
            self.max_heapify(i)
            
    def sort(self):
        self.build_max_heap()
        for i in range(self.heap_size, 1, -1):
            tmp = self.arr[0]
            self.arr[0] = self.arr[self.heap_size-1]
            self.arr[self.heap_size-1] = tmp
            self.heap_size += -1
            self.max_heapify(1)

class min_heap():
    def __init__(self, arr):
        self.arr = arr
        self.heap_size = len(arr)
        self.heap_length = len(arr)
        
    def min_heapify(self, i):
        left = 2*i
        right = 2*i + 1
        smallest = i
        
        if left <= self.heap_size:
            if self.arr[left-1] < self.arr[smallest-1]:
                smallest = left
        if right <= self.heap_size:
            if self.arr[right-1] < self.arr[smallest-1]:
                smallest = right
        if smallest != i:
            tmp = self.arr[smallest - 1]
            self.arr[smallest-1] = self.arr[i-1]
            self.arr[i-1] = tmp
            self.min_heapify(smallest)
            
    def build_min_heap(self):
        nonleaf = int(self.heap_length/2)
        for i in range(nonleaf, 0, -1):
            self.min_heapify(i)
            
    def sort(self):
        self.build_min_heap()
        for i in range(self.heap_size, 1, -1):
            tmp = self.arr[0]
            self.arr[0] = self.arr[self.heap_size-1]
            self.arr[self.heap_size-1] = tmp
            self.heap_size += -1
            self.min_heapify(1)
