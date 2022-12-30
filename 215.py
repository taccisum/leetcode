from typing import List

def shuffer(nums):
    from random import randint
    for i in range(len(nums)):
        j = randint(0, len(nums) - 1)
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
    return nums


def findKthLargest(nums: List[int], k: int) -> int:
    shuffer(nums)       # 先打乱数组，避免极端情况下性能退化到 O(n)
    lowk = len(nums) - k        # 找第 k 大，就是等价于找第 size-k 小

    def find(nums, l, r):
        first=l; last=r-1; pivot=nums[first]

        while first < last:
            while first < last and nums[last] >= pivot:
                last-=1
            nums[first] = nums[last]
            while first < last and nums[first] <= pivot:
                first+=1
            nums[last] = nums[first]
        nums[first]=pivot

        if first == lowk: return pivot

        if first > lowk:
            # 继续在左边找
            return find(nums, l, first)
        else:
            # 否则在右边找
            return find(nums, first+1, r)

    return find(nums, 0, len(nums))


if __name__ == '__main__':
    # print(shuffer([1,2,3,4,5,6,7,8]))
    print(findKthLargest([3,2,1,5,6,4], 2))
    print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))
    print(findKthLargest([2,1], 2))
