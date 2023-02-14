# https://leetcode.cn/problems/word-break/


from typing import List


class Solution:
    def integerBreak(self, n: int) -> int:
        dp_size = max(n, 4)
        dp = [ 0 for i in range(dp_size+1)]
        dp[0]=0; dp[1]=0; dp[2]=1; dp[3]=2; dp[4]=4
        if n < 5: return dp[n]

        for i in range(5, n+1):
            max_=0
            for j in range(1, i):
                max_=max(max_, j*dp[i-j])
                max_=max(max_, j*(i-j))
            dp[i] = max_
        print(dp)
        return dp[n]


if __name__ == '__main__':
    s=Solution()
    assert s.integerBreak(3) == 2
    assert s.integerBreak(4) == 4
    assert s.integerBreak(5) == 6
    assert s.integerBreak(10) == 36
    assert s.integerBreak(100) == 7412080755407364
