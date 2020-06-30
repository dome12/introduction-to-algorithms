"""
Created on Tue Jun 30 11:09:40 2020
@author: domerose

堆是什么？ 用数组来近似完全二叉树的一种数据结构
属性：
    heap_size -> 堆有效的数据量
    heap_length -> 堆的最大数据容量
    结点-> 父节点（int(i/2)）以及 子结点（左结点（2*i）右结点（2*i+1））
    根节点 -> 二叉树的顶端，最上面的那个结点。无父节点，但有子节点。
    叶节点 -> 二叉树的末端，最小面的结点。有父节点，但无子节点（意味着没有左结点，也没有右结点）int(n/2)之后的结点, in(n/2)+1 .... n 都是叶节点
    > 考虑一个结点如果有左结点，那么它就不可能是叶节点。所以若该节点是叶节点，则 2*i > n. 若n是偶数，那么i > n/2; 若n是奇数, 那么i> n/2,  n/2 位于（int(in/2), int(in/2)+1）。
        综上 i <= int(n/2)，为非叶结点。
    堆的高度。指从当前结点到叶节点的最长路径。
    堆的层：也就是结点所处二叉树的层->叶节点所处二叉树的层。2**k , k代表了结点所在的层数。
    堆的高度：root -> leaf 的最长路径
    
"""
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
