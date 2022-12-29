from math import floor
from typing import List


def singleNonDuplicate(nums: List[int]):
    l=0; r=len(nums); len_=r

    while l < r:
        mid = floor((l+r)/2)
        llen = mid      # mid 为下标，mid 左边的元素个数刚好等于 mid 的下标值
        # print(l, r, mid, llen)

        has_l = mid - 1 >= 0
        has_r = mid + 1 < len_
        leq = False if not has_r else nums[mid] == nums[mid-1]      # 表示 mid 是否与左相邻元素相等
        req = False if not has_r else nums[mid] == nums[mid+1]      # 表示 mid 是否与右相邻元素相等

        if has_l and has_r:
            if not leq and not req: return nums[mid]
        elif has_l and not has_r:
            if not leq: return nums[mid]
        elif has_r and not has_l:
            if not req: return nums[mid]
        else:
            return nums[mid]

        if not leq and llen % 2 == 0:
            # 如果 mid 与左边相邻元素相等，则期望 llen 为偶数
            # 说明落单数在右边，继续找
            l = mid
        elif leq and llen % 2 == 1:
            # 如果 mid 与右边相邻元素相等，则期望 llen 为奇数
            # 说明落单数在右边，继续找
            l = mid
        else:
            # 说明落单数在左边，继续找
            r = mid

    # 跳出循环了，说明不存在落单数
    return None


if __name__ == '__main__':
    print(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
    print(singleNonDuplicate([3,3,7,7,10,11,11]))

    # leetcode 特殊用例
    print(singleNonDuplicate([1]))
    print(singleNonDuplicate([1,1,2]))
    print(singleNonDuplicate([1,2,2,3,3]))
    print(singleNonDuplicate([1,1,2,2,4,4,5,5,9]))
