def test_sort(cls, arr):
    cls(arr)
    print(arr)
    print(is_sorted(arr))


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
        judge.add(cmp(i, i + 1))
        if 1 in judge and -1 in judge:
            return False
    return True