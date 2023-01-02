# https://leetcode.cn/problems/climbing-stairs/


def climbStairs(n: int) -> int:
    if n < 2: return n

    dp=[1 for i in range(n+1)]      # dp 数组，存储计算过的结果
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]       # 状态转移方程
    return dp[n]


def climbStairsO1MemoryEdition(n: int) -> int:
    """
    dp O(1) 空间复杂度版本
    """
    if n < 2: return n

    p1=1; p2=1; dp=2
    for i in range(2, n+1):
        dp=p1+p2       # 状态转移方程
        p2=p1
        p1=dp
    return dp


if __name__ == '__main__':
    print(climbStairsO1MemoryEdition(10))     # print 89
    print(climbStairsO1MemoryEdition(100))    # print 573147844013817084101
