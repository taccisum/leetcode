# https://leetcode.cn/problems/house-robber/

from typing import List


def rob(nums: List[int]) -> int:
    if len(nums)<=2: return max(nums)
    dp=[0 for i in range(len(nums))]; dp[0]=nums[0]; dp[1]=max(nums[0:2])
    for i in range(2, len(nums)): dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    return dp[-1]


if __name__ == '__main__':
    print(rob([2,7,9,3,1]))     # print 12
    print(rob([0]))     # print 0
