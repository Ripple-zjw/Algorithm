# 优先队列
# 大顶堆

from Heap.HeapSort import HeapSort
from Heap.HeapSort_small import HeapSortSmall


class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.heap_size = 0

    def insert(self, v):
        '''
        :param v: 需要插入的元素
        :return: None
        '''
        self.heap_size += 1
        self.heap.append(0)
        self.increase_key(self.heap_size - 1, v)

    def maximum(self):
        '''
        :return: 返回堆中的最大值
        '''
        if self.heap_size == 0:
            return None
        return self.heap[0]

    def extract_max(self):
        '''

        :return: 返回并拿出堆中的最大值
        '''
        if self.heap_size <= 0:
            return None
        ans = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap_size -= 1
        self.maxHeapify(0)
        return ans

    def increase_key(self, i, k):
        '''
        选择一个下标，将其值改变，并且重新整理大顶堆
        :param i: 需要改变的索引
        :param k: 改变的值
        :return: None
        '''
        if self.heap[i] < k:
            self.heap[i] = k
            while i > 0 and self.heap[i] > self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
                i = i // 2
        else:
            self.heap[i] = k
            self.maxHeapify(i)

    def maxHeapify(self, i):
        '''
        整理大顶堆的关键方法
        :param i: 下标
        :return: None
        '''
        left = 2 * (i + 1) - 1
        right = 2 * (i + 1)
        largest = i
        if left < self.heap_size and self.heap[largest] < self.heap[left]:
            largest = left
        if right < self.heap_size and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != i:
            self.heap[largest], self.heap[i] = self.heap[i], self.heap[largest]
            self.maxHeapify(largest)

    def heapSort(self, reverse=False):
        '''
        将堆中的元素排序，默认从小到大。
        :param reverse:使数组从大到小排序
        :return: 重新返回一个列表，不改变原来的堆。
        '''
        sort_heap = self.heap[:]
        if reverse:
            HeapSortSmall(sort_heap)
        else:
            HeapSort(sort_heap)
        return sort_heap


if __name__ == '__main__':
    pq = PriorityQueue()
    for i in range(13):
        pq.insert(i)
    print(pq.heap)
    # print(pq.heap_size)
    # pq.increase_key(4, 13)
    # print(pq.heap)
    # print(pq.heap_size)
    # print(pq.extract_max())
    # print(pq.heap)
    # print(pq.maximum())
    # pq.increase_key(0, 0)
    # print(pq.heap)
    # print(pq.heap_size)
    print(pq.heapSort())
    print(pq.heap)
    print(pq.heapSort(reverse=True))
    print(pq.heap)
