def test_sort(cls, arr):
    cls(arr)
    print(arr)
    print(is_sorted(arr))


def CountingSortTest(obj, arr):
    test = obj()
    ans = test.sort(arr)
    print(ans)
    print(is_sorted(ans))


def bucket_sort(obj, arr, n, length=1, mod=1, divi=1):
    res = obj.bucket_sort(arr, n, length, mod, divi)
    print(res)
    print(is_sorted(res))


def is_sorted(arr) -> bool:
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
