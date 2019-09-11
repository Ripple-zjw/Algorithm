# 堆排序
# 从大到小排序
# 小顶堆


class HeapSortSmall:
    def __init__(self, heap):
        self.length = len(heap)
        self.heapSort(heap)

    def minHeapify(self, i, heap):
        left = 2 * (i + 1) - 1
        right = 2 * (i + 1)
        smallest = i
        if left < self.length and heap[smallest] > heap[left]:
            smallest = left
        if right < self.length and heap[smallest] > heap[right]:
            smallest = right
        if i != smallest:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            self.minHeapify(smallest, heap)

    def buildSmallHeap(self, heap):
        for i in range(self.length // 2 - 1, -1, -1):
            self.minHeapify(i, heap)

    def heapSort(self, heap):
        self.buildSmallHeap(heap)
        for i in range(self.length - 1, 0, -1):
            heap[0], heap[i] = heap[i], heap[0]
            self.length -= 1
            self.minHeapify(0, heap)


if __name__ == '__main__':
    arr = [1, 3, 4, 2, 1, 3, 45, 5, 6, 8, 10, 11, 12, 13, 14, 15, 30, 31, 4, 6, 2, 3, 45, 1, 2, 3, 6, 7, 4, 4]
    HeapSortSmall(arr)
    print(arr)
    arr1 = [1, 5, 4, 2, 5, 6, 7, 3, 4, 9, 1, 23, 6, 4, 2, 88, 4]
    HeapSortSmall(arr1)
    print(arr1)
    arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    HeapSortSmall(arr2)
    print(arr2)
