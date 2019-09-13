class CountingSort(object):
    def sort(self, arr):
        return self.counting_sort(arr, max(arr))

    def counting_sort(self, arr, maxNum):
        hashTable = [0 for _ in range(maxNum + 1)]
        ans = [0 for _ in range(len(arr))]
        for num in arr:
            hashTable[num] += 1
        for i in range(1, len(hashTable)):
            hashTable[i] = hashTable[i - 1] + hashTable[i]
        for j in range(len(arr) - 1, -1, -1):
            ans[hashTable[arr[j]] - 1] = arr[j]
            hashTable[arr[j]] -= 1
        return ans


if __name__ == '__main__':
    from Sort.test import CountingSortTest

    CountingSortTest(CountingSort, [2, 5, 3, 0, 2, 3, 0, 3])
    CountingSortTest(CountingSort, [100, 23, 4, 3, 2, 6, 88, 5, 9, 1, 4, 3, 6])
    CountingSortTest(CountingSort, [1000, 34, 666, 4, 3, 4, 26, 634, 7, 57, 3, 52, 5, 3, 0, 2, 3, 0, 3])
    # 当数组的元素值太大时，速度回非常慢。。。
    # CountingSortTest(CountingSort, [100000000, 100000, 2, 5, 3, 0, 2, 3, 0, 3])
    # 极大占用内存。
    # CountingSortTest(CountingSort, [1000000000])
