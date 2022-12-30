from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
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
    print(findKthLargest([3,2,1,5,6,4], 2))
    print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))
    print(findKthLargest([2,1], 2))
