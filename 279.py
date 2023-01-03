# https://leetcode.cn/problems/perfect-squares/


from typing import List

dp_cache:List=None

class Solution:
    def numSquares(self, n: int) -> int:
        global dp_cache
        if dp_cache is not None and len(dp_cache) > n:
            return dp_cache[n]

        dp=[ i for i in range(n+1) ]

        base=2
        for i in range(4, n+1):
            if base**2==i: dp[i]=1; base+=1; continue     # 当前数刚好等于 base 的平方，置 1

            """
            嵌套 for 循环法, O(n^2) 时间复杂度, leetcode 运行会超时
            """
            # min_=dp[i]
            # for j in range(1, i+1):
            #     min_=min(dp[j]+dp[i-j], min_)
            # dp[i]=min_

            """
            仔细观察规律，还可以发现一种将内循环复杂度降低为 O(sqrt(n)) 的方法
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
            以 26 为例，只可能存在下列拆解组合
            26=5*2+1
            26=4*2+9
            26=3*2+16
            26=2*2+22
            26=1*2+25
            显然 dp[25]=dp[16]=dp[9]=dp[4]=dp[1]=1
            因此 dp[26]=min(dp[1], dp[9], dp[16], dp[22], dp[25])+1
            """
            min_=dp[i]
            for j in range(1, base):
                min_=min(dp[j**2]+dp[i-j**2], min_)
            dp[i]=min_

        dp_cache=dp
        return dp[n]


if __name__ == '__main__':
    s=Solution()
    assert s.numSquares(1) == 1
    assert s.numSquares(2) == 2
    assert s.numSquares(3) == 3
    assert s.numSquares(6) == 3
    assert s.numSquares(12) == 3
    assert s.numSquares(13) == 2
    assert s.numSquares(25) == 1
    assert s.numSquares(26) == 2
else:
    Solution().numSquares(5000)   # 如果跑 leetcode，先全局计算一次 cache 起来，可以避免大量重复运算 
