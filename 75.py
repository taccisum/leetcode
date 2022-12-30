# https://leetcode.cn/problems/sort-colors/

from typing import List


def sortColors(nums: List[int]) -> None:
    count_bucket = [0 for i in range(3)]
    for n in nums: count_bucket[n]+=1

    i=0
    for j in range(3):
        for k in range(count_bucket[j]):
            nums[i]=j; i+=1
    print(nums)


if __name__ == '__main__':
    sortColors([2,0,2,1,1,0])
    sortColors([2,0,1])
