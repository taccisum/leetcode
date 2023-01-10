# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/


from typing import List


class Solution:
    """
    双指针法，未能完全通过用例(186/211)，且过于复杂
    """
    def maxProfit(self, prices: List[int]) -> int:
        l=0; r=len(prices)-1; l_val=prices[0]; r_val=prices[-1]

        max_=max(r_val-l_val, 0)
        l_end=False; r_end=False
        while l<r:
            l0=l
            while not l_end and  l<r and prices[l] >= l_val: l+=1
            if l<r: l_val=prices[l]; max_=max(r_val-l_val, max_)
            else: l=l0; l_end=True
            print(l, r, r_val, '-', l_val, '=', max_)

            r0=r
            while not r_end and l<r and prices[r] <= r_val: r-=1
            if l<r: r_val=prices[r]; max_=max(r_val-l_val, max_)
            else: r=r0; r_end=True

            print(l, r, r_val, '-', l_val, '=', max_)
            if l_end and r_end: break
        return max_


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp 解法，时间复杂度为 O(n)
        """
        max_price=0; dp=[ 9999 for i in range(len(prices)) ]    # dp[i] 表示前 i 天中的最低价格

        for i in range(len(prices)):
            dp[i]=dp[i-1] if dp[i-1] < prices[i] else prices[i]
            max_price=max(max_price, prices[i]-dp[i])
        # print(dp)
        return max_price

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp 解法 + 空间压缩，时间复杂度为 O(n)
        """
        max_price=0; p1=9999; cp=9999
        for i in range(len(prices)):
            p1=cp; cp=min(p1, prices[i])
            max_price=max(max_price, prices[i]-cp)
        return max_price

if __name__ == '__main__':
    s=Solution()
    assert s.maxProfit([7,1,5,3,6,4]) == 5
    assert s.maxProfit([1,2]) == 1
    assert s.maxProfit([7,6,4,3,1]) == 0
    assert s.maxProfit([1,4,2]) == 3
    assert s.maxProfit([3,2,6,5,0,3]) == 4
    assert s.maxProfit([2,1,2,1,0,1,2]) == 2
    assert s.maxProfit([2,7,1,4]) == 5
    
