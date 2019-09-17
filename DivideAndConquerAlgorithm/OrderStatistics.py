# 顺序统计量
# 第k小（大）元素
from random import randint


class OrderStatistics:
    def calculate(self, arr, k):
        return self.order_statistics(0, len(arr) - 1, arr, k)

    def order_statistics(self, l, r, arr, i):
        if l == r:
            return arr[l]
        pivot = self.partition(l, r, arr)
        k = pivot - l + 1
        if k == i:
            return arr[pivot]
        elif k > i:
            return self.order_statistics(l, pivot - 1, arr, i)
        else:
            return self.order_statistics(pivot + 1, r, arr, i - k)

    def partition(self, l, r, arr):
        pivot = randint(l, r)
        arr[pivot], arr[r] = arr[r], arr[pivot]
        pivot = arr[r]
        i = l - 1
        for j in range(l, r):
            if arr[j] < pivot:  # 如果要统计第k大元素那么把小于改为大于。
                i += 1
                arr[j], arr[i] = arr[i], arr[j]
        arr[i + 1], arr[r] = arr[r], arr[i + 1]
        return i + 1


if __name__ == '__main__':
    from DivideAndConquerAlgorithm.test import Test

    test = Test()
    for i in range(1, 10):
        test.order_statistics(OrderStatistics, [3, 4, 6, 1, 4, 7, 9, 54, 4], i)

    for i in range(1, 11):
        test.order_statistics(OrderStatistics, [4, 55, 213, 453, 423, 22, 54, 674, 12, 65], i)

    test.order_statistics(OrderStatistics, [3, 2, 1, 5, 6, 4], 3)
