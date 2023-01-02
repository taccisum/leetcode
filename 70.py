# https://leetcode.cn/problems/climbing-stairs/


def climbStairs(n: int) -> int:
    if n < 2: return n

    dp=[1 for i in range(n+1)]
    for i in range(2, n+1): dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


if __name__ == '__main__':
    print(climbStairs(10))
    print(climbStairs(100))
