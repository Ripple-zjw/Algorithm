class Test:
    def quick_sort(self, cls, arr):
        cls(arr)
        print(arr)
        print(self.is_sorted(arr))

    def counting_sort(self, obj, arr):
        test = obj()
        ans = test.sort(arr)
        print(ans)
        print(self.is_sorted(ans))

    def bucket_sort(self, obj, arr, n, length=1, mod=float('inf')):
        res = obj()
        ans = res.bucket_sort(arr, n, length, mod)
        print(ans)
        print(self.is_sorted(ans))

    def is_sorted(self, arr) -> bool:
        def cmp(a, b):
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0

        judge = set()
        for i in range(len(arr) - 1):
            judge.add(cmp(arr[i], arr[i + 1]))
            if 1 in judge and -1 in judge:
                return False
        return True
