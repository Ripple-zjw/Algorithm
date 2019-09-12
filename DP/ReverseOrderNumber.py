from DP.test import cal_test


class ReverseOrderNumber:
    def calculate(self, string: str) -> int:
        length = len(string)
        dp = [0 for _ in range(10)]
        ans = []
        for i in range(length):
            tmp = int(string[i])
            dp[tmp] += 1
            res = 0
            for j in range(tmp + 1, len(dp)):
                res += dp[j]
            ans.append(res)
        return sum(ans)


if __name__ == '__main__':
    test = ReverseOrderNumber()
    # cal_test(test, '32514')
    # cal_test(test, '12345')
    # cal_test(test, '13578642')
    # cal_test(test, '135642')
    # cal_test(test, '1342')
    # cal_test(test, '1234')
    # cal_test(test, '4132')
    # cal_test(test, '3421')
    # cal_test(test, '2413')
    # cal_test(test, '332581')
    # cal_test(test, '9876543210')
    cal_test(test, '3123124124355665645786786786456324523426456456745768885948949156198498797161948900041727794415646')
