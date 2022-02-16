import numpy


def process(money, target, index):
    if target < 0:
        return float('inf')
    if index == len(money):
        return 0 if target == 0 else float('inf')
    p1 = process(money, target, index + 1)
    p2 = 1 + process(money, target - money[index], index + 1)
    return min(p1, p2)


def main(money, target):
    return process(money, target, 0)


def findmoney_withcounts_dp(money, counts, target):
    M = len(money)
    N = target
    dp = [[0] * (N + 1) for _ in range(M + 1)]
    # dp = numpy.full((M+1, N+1), 0)
    dp[M][0] = 1
    for i in range(M - 1, -1, -1):
        for j in range(N + 1):
            dp[i][j] = dp[i + 1][j]
            if j - money[i] >= 0:
                if j - money[i] * (counts[i] + 1) >= 0:
                    dp[i][j] += dp[i][j - money[i]] - dp[i + 1][j - (counts[i] + 1) * money[i]]
                else:
                    dp[i][j] += dp[i][j - money[i]]
    return dp[0][N]


if __name__ == '__main__':
    money = [5, 5, 5, 20, 30]
    # counts = [11, 5, 10]
    target = 50
    print(main(money, target))
