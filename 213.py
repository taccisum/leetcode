# https://leetcode.cn/problemset/all/?page=1&search=474


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3: return max(nums)
        # dp 代表前 i 间房可以获得的最大金额
        dp=[ 0 for i in range(len(nums)) ]; dp[0]=nums[0]
        # 这里还需要用到一个辅助的 dp2 数组，其中 dp2[i] 代表不抢首间房的前提下，前 i 间房可以获得的最大金额
        dp2=[ 0 for i in range(len(nums)) ]; dp2[0]=0

        for i in range(1, len(nums)-1):
            # 针对非最后一间房，有两种选择，取金额最大的一种
            # choice1: 如果选择抢第 i 间房屋，那么第 i-1 间房就必然不能抢，因此 dp[i]=dp[i-2]+nums[i]
            # choice2: 如果选择不抢第 i 间房，dp[i]=dp[i-1]
            c1=dp[i-2]+nums[i]; c2=dp[i-1]
            dp[i]=max(c1, c2); dp2[i]=max(dp2[i-2]+nums[i], dp2[i-1])

        # 针对最后一间房，需要考虑首尾相连的情况，也有两种选择
        # choice1: 如果抢最后一间房，那么首间房必不能抢，此时 dp[i]=max(dp2[i-2]+nums[i])
        # choice2: 如果不抢最后一间房，显然 dp[i]=dp[i-1]
        dp[-1]=max(dp2[-3]+nums[-1], dp[-2])

        # print(dp, dp2)
        return dp[-1]

if __name__ == '__main__':
    s=Solution()
    # assert s.rob([10,9,2,5,3,7,101,18]) == 4
    assert s.rob([2,3,2]) == 3
    assert s.rob([2,3,2,4]) == 7
    assert s.rob([200,3,140,20,10]) == 340
