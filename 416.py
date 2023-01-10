# https://leetcode.cn/problems/partition-equal-subset-sum/


from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_=sum(nums)
        if sum_%2 != 0: return False
        h=len(nums)+1; w=int(sum_/2)+1      # 计算 dp 的宽高
        dp=[[False]*w for i in range(h)]
        dp[0][0]=True       # 前 0 个数构成 0，显然是可以的

        # dp[i][j] 表示子数组 nums[:i] 中是否存在元素之和为 j 的子序列
        for i in range(1, h):
            num=nums[i-1]
            for j in range(w):
                if j-num >= 0:
                    # j-num>=0，说明 num 本身比目标数 j 要小，此时分两种情况
                    # 1. 要这个数 num，则 dp[i][j]=dp[i-1][j-num]，即前 i-1 个数是否存在子序列和为 j-num
                    # 2. 不要这个数 num，则 dp[i][j]=dp[i-1][j]，即前 i-1 个数是否存在子序列和为 j
                    dp[i][j]=dp[i-1][j-num] or dp[i-1][j]
                else:
                    # 如果 j-num<0，说明 num 本身比目标数 j 还要大，那只能不要这个数了，因此 dp[i][j]=dp[i-1][j]
                    dp[i][j] = dp[i-1][j]

        # import numpy as np
        # print(np.array(dp))
        return dp[-1][-1]


if __name__ == '__main__':
    s=Solution()
    assert s.canPartition([1,5,11,5])
    assert not s.canPartition([1,2,3,5])
