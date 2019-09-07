class HeapSort(object):
    def __init__(self, arr):
        self.length = len(arr)
        self.heapSort(arr)

    def maxHeapify(self, arr, i):
        left = 2 * i
        right = 2 * i + 1
        largest = i
        if left < self.length and arr[i] < arr[left]:
            largest = left
        if right < self.length and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.maxHeapify(arr, largest)

    def buildMaxHeap(self, arr):
        for i in range(len(arr) // 2 - 1, -1, -1):
            self.maxHeapify(arr, i)

    def heapSort(self, arr):
        self.buildMaxHeap(arr)
        for i in range(len(arr) - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.length -= 1
            self.maxHeapify(arr, 0)


if __name__ == "__main__":
    arr = [1, 3, 4, 2, 1, 3, 45, 5, 6, 8, 10, 11, 12, 13, 14, 15, 30, 31, 4, 6, 2, 3, 45, 1, 2, 3, 6, 7, 4, 4]
    sor = HeapSort(arr)
    print(arr)
