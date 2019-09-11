from random import randint

from test import test_sort


class QuickSort:
    def __init__(self, arr):
        self.quick_sort(arr, 0, len(arr) - 1)

    def quick_sort(self, arr, start, end):
        if start < end:
            pivot = self.partition(arr, start, end)
            self.quick_sort(arr, start, pivot - 1)
            self.quick_sort(arr, pivot + 1, end)

    def partition(self, arr, start, end):
        pivot = randint(start, end)
        arr[pivot], arr[end] = arr[end], arr[pivot]
        pivot = arr[end]
        i = start - 1
        for j in range(start, end):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[end] = arr[end], arr[i + 1]
        return i + 1


if __name__ == "__main__":
    test_sort(QuickSort, [3, 4, 2, 5, 6, 7, 22, 11, 4, 1, 1])
    test_sort(QuickSort, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    test_sort(QuickSort, [1, 3, 4, 2, 1, 3, 45, 5, 6, 8, 10, 11, 12, 13, 14, 15, 30, 31, 4, 6, 2, 3, 45, 1, 2, 3, 6, 7, 4, 4])
    test_sort(QuickSort, [1, 5, 4, 2, 5, 6, 7, 3, 4, 9, 1, 23, 6, 4, 2, 88, 4])
    test_sort(QuickSort, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    test_sort(QuickSort, [2, 8, 7, 1, 3, 5, 6, 4])
