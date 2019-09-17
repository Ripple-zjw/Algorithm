class Test:
    def order_statistics(self, cls, arr, k):
        test = cls()
        ans = test.calculate(arr, k)
        print(ans)
        print(ans == sorted(arr)[k - 1])
