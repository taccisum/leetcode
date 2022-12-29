from math import ceil, floor

def find_bound(nums, target):
    """
    注意：此算法尚未经 leetcode 用例验证
    """
    return lower_bound(nums, target), upper_bound(nums, target)


def lower_bound(nums, target):
    l=0; r=len(nums)        # 这里采用左闭右开原则 [l,r)

    while l < r:
        mid = floor((l+r) / 2)
        if nums[mid] >= target:
            # 中间值大于或等于要找的目标值，收缩右边界
            r = mid
        else:
            # 中间值小于要找的目标值，收缩左边界
            # 已知 nums[mid] 不为 target，l 可直接置为 mid + 1，同时也有助于避免无限循环
            l = mid + 1

    return l


def upper_bound(nums, target):
    # 逻辑刚好与找 lower_bound 相反
    l=0; r=len(nums) - 1

    while l < r:
        mid = ceil((l+r) / 2)
        if nums[mid] <= target:
            l = mid
        else:
            r = mid - 1

    return r


if __name__ == '__main__':
    print(lower_bound([7,8,8,10], 8))   # print 1
    print(lower_bound([5,7,7,8,8,10], 8))   # print 3
    print(lower_bound([1,2,2,3,3,5,6,6,7,7,8,8,10], 8))     # print 10
    print(upper_bound([1,2,2,3,3,5,6,6,7,7,8,8,10,11,13], 8))
    print(upper_bound([1,2,2,3,3,5,6,6,7,7,8,8,8,8,10,11,13], 8))
    arr = [1,2,2,3,3,5,6,6,7,7,8,8,8,8,10,11,13]
    print(find_bound(arr, 8), arr[10:13+1])
