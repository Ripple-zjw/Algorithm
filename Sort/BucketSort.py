class BucketSort:
    def bucket_sort(self, arr, space, length=1, mod=float('inf'), divi=1):
        '''
        这个函数是用桶排序完成的，效率取决于是否能将每个数均匀的放在你申请的桶中。
        每个桶内部的排序是依靠二分查找加insert的方法，时间复杂度应该在O(nlogn)
        比如你要排的数全都是0-1之间的小数，你就可以让length为10，这样数组中的数都是在10以内，space为10就行了。
        再比如你要排的数在9900-10000之间，你无需声明一个10000长度的数组，只要将mod为100，这样数组中的数都是在100以内
        的数space为100就行了。
        至于如何能把效率变为最大，要看数的范围，如果100-100000之间，数大部分集中在100-1000之间，那么桶排序的效率不高，
        你可以把1000个划分为一个桶，再把数量最多的1-1000内再继续划分。但这个函数做不到。。。
        :param arr: 你需要排序的数组。
        :param space: 申请多大的空间(桶)，最小也要是arr中最大的值+1，当length为1时。
        :param length: 是一个乘数，将数组中的每个数乘以length，得到的值不能超过space的大小。
        :param mod: 取余操作，和length一样，将数组中的每个数对mod取余,得到的值不能超过space的大小。
        :param divi: 除法操作，和length，mod一样，将数组中的每个数除以divi，得到的值不能超过space的大小。
        :return: 返回的结果是一个列表
        '''
        tmp = [[] for _ in range(space)]
        for num in arr:
            ind = int(num * length) % mod // divi
            if len(tmp[ind]) == 0:
                tmp[ind].append(num)
            else:
                left = 0
                right = len(tmp[ind]) - 1
                while left <= right:
                    mid = left + ((right - left) // 2)
                    if tmp[ind][mid] == num:
                        tmp[ind].insert(mid, num)
                    elif tmp[ind][mid] > num:
                        right = mid - 1
                    else:
                        left = mid + 1
                tmp[ind].insert(left, num)
        return [x for _ in tmp for x in _]


if __name__ == '__main__':
    from Sort.test import bucket_sort

    test = BucketSort()
    bucket_sort(test, [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68], 10, 10)
    bucket_sort(test, [0.3, 0.4, 0.1, 0.22, 0.36, 0.8, 0.99, 0.12, 0.111, 0.123], 10, 10)
    bucket_sort(test, [1.2, 1.3, 1.55, 1.33, 1.02, 1.00, 1.32], 20, 10)
    bucket_sort(test, [2, 34, 1, 4, 5, 67, 45, 78, 5, 75, 6, 45, 64, 34, 2, 36, 62, 12, 46, 8, 54, 43, 12], 8, 0.1)
    bucket_sort(test, [9990, 9994, 9991, 9990, 9997, 9993, 9993, 9998, 9997, 9995, 9999, 9999, 9997, 9996], 10, mod=10)
    bucket_sort(test,
                [1002, 1004, 1104, 1306, 4098, 3054, 2065, 6666, 5505, 7717, 9981, 7749, 8864, 6636, 5525, 4416, 3309,
                 8812, 8745],
                10,
                divi=1000
                )
