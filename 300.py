# https://leetcode.cn/problems/longest-increasing-subsequence/


from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        两次嵌套循环 + dp, 时间复杂度 O(n^2)

        这题的核心难点在于 dp[i] 的定义
        - 如果把 dp[i] 定义为 nums[:i+1] 的最大子序列长度, 那我们将很难找出状态转移方程
        - 但如果把 dp[i] 定义为以 nums[i] 结尾的子序列最大长度，就很容易了
        """
        if len(nums) <= 1: return len(nums)
        dp=[ 1 for i in range(len(nums)) ]      # dp[i] 表示以 i 结尾的最长子序列长度
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]: dp[i]=max(dp[j]+1, dp[i])
        # print(dp)
        return max(dp)

if __name__ == '__main__':
    s=Solution()
    assert s.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
    assert s.lengthOfLIS([1,2,3,4,5,6,2,3,4,7,8,9]) == 9
    assert s.lengthOfLIS([1,2,3,4,5,6,-2,-1,0,1,2,3,4,7,8,9]) == 10
    assert s.lengthOfLIS([10,9,2,5,3,4]) == 3
    assert s.lengthOfLIS([0,1,0,3,2,3]) == 4
    assert s.lengthOfLIS([4,10,4,3,8,9]) == 3
    assert s.lengthOfLIS([1,3,6,7,9,4,10,5,6]) == 6
    
    # 1,2,2,2,
