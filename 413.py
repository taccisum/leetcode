# https://leetcode.cn/problems/arithmetic-slices/

from typing import List


def numberOfArithmeticSlicesDpEdition(nums: List[int]) -> int:
    """
    dp 解法 O(n)

    在一个长度为 n 的等差数列中，长度为 k 的连续子序列数量为
    c(n=n)=1
    c(n=n-1)=2
    c(n=n-2)=3
    c(n=k)=n-k+1
    即这里的规律是长度每 +1, 子序列的数量就 -1

    所以，如果我们能在数组 nums 中找到一个长度为 n 的等差数列, 那么他的长度 >=3 的等差子序列数量其实是固定的
    假设该子序列的起止区域为 [i, j) 且 j-i=k=n-2, 则有
    dp[i]=c(n=n)=1
    dp[i+1]=c(n=n-1)=2
    ...
    dp[j]=c(n=3)=n-(j-i)+1
    """

    dp=[0 for i in range(len(nums))]
    for i in range(2, len(nums)):   # 从下标 2 开始是因为子序列长度至少为 3
        if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
            # 说明这个等差数列还能往右扩张
            dp[i] = dp[i-1]+1
    return sum(dp)


def numberOfArithmeticSlices0(nums: List[int]) -> int:
    """
    暴力解法 O(n^2)
    """
    count=[0 for i in range(len(nums))]

    for i in range(len(nums)):
        for j in range(i+2, len(nums)):
            # 子数组长度至少为 3 才有意义
            if nums[j]-nums[j-1] == nums[j-1]-nums[j-2]: count[i]+=1

    return sum(count)


if __name__ == '__main__':
    # numberOfArithmeticSlices=numberOfArithmeticSlices0
    numberOfArithmeticSlices=numberOfArithmeticSlicesDpEdition
    print(numberOfArithmeticSlices([1,2,3,4]))
    print(numberOfArithmeticSlices([7,7,7,7]))
    print(numberOfArithmeticSlices([1,3,5,7,9]))
    print(numberOfArithmeticSlices([1,2,3,4,5,6,7]))
    print(numberOfArithmeticSlices([0]))
    print(numberOfArithmeticSlices([0,1]))
