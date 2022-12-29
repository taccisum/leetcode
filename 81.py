from math import floor


def bisearch(nums, target, l=None, r=None):
    l=0 if l is None else l
    r=len(nums) if r is None else r

    while l + 1 < r:
        mid=floor((l+r)/2)
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            r = mid
        else:
            l = mid
    return False


def search(nums, target, l=None, r=None):
    """
    [Deprecated!]
    注意：此版本未经 leetcode 用例验证
    """
    l=0 if l is None else l
    r=len(nums) if r is None else r
    mid=floor((l+r)/2)
    # print(l, r, mid)

    if l >= r:
        return False
    if nums[mid] == target:
        return True

    if nums[mid] <= nums[r-1]:
        # 右边排好序
        if target <= nums[r-1]:
            # 目标值小于右边最大值，说明目标值只可能在右边
            return bisearch(nums, target, mid, r)
        else:
            # 否则对左边继续递归搜索
            return search(nums, target, l, mid)
    else:
        # 右边无序，那左边必然有序
        if target >= nums[l]:
            # 目标值大于右边最小值，说明目标值只可能在左边
            return bisearch(nums, target, l, mid)
        else:
            # 否则对右边继续递归搜索
            return search(nums, target, mid, r)

def search_non_recu(nums, target):
    # 非递归版本
    l = 0; r = len(nums)        # 左开右闭

    while l < r:
        mid = floor((l + r) / 2)
        # print(l, r, mid)
        if nums[mid] == target:
            return True

        # 无法判断哪边有序，逐位增减
        if nums[l] == nums[mid]:
            l+=1
            continue
        elif nums[mid] == nums[r-1]:
            r-=1
            continue
        
        if nums[mid] > nums[l]:
            # mid 严格大于 left，认为左边有序
            if target >= nums[l] and target <= nums[mid-1]:
                # 目标值在左区间，左区间是有序的
                r = mid
            else:
                # 目标值在右区间，右区间是无序的
                l = mid + 1
        elif nums[mid] < nums[r-1]:
            # mid 严格小于 right，认为右边有序
            if target >= nums[mid] and target <= nums[r-1]:
                # 目标值在右区间，右区间是有序的
                l = mid + 1
            else:
                # 目标值在左区间，左区间是无序的
                r = mid

    # 跳出循环了，说明没找到
    return False


if __name__ == '__main__':
    # print True
    print(search_non_recu([2,5,6,0,0,1,2], 0))
    print(search_non_recu([2,5,6,0,0,1,2], 1))
    print(search_non_recu([2,5,6,0,0,1,2], 2))
    print(search_non_recu([2,5,6,0,0,1,2], 5))
    print(search_non_recu([2,5,6,0,0,1,2], 6))


    # print False
    print(search_non_recu([2,5,6,0,0,1,2], 7))
    print(search_non_recu([2,5,6,0,0,1,2], 3))
    print(search_non_recu([2,5,6,0,0,1,2], 10))
    print(search_non_recu([2,5,6,0,0,1,2], -1))

    # leetcode 特殊用例
    print(search_non_recu([1,0,1,1,1], 0))      # True
    print(search_non_recu([1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1], 13))      # True

    # print(bisearch([0,0,1,2], 0))
    # print(bisearch([0,0,1,2], 2))
    # print(bisearch([0,0,1,2], 1))
    # print(bisearch([0,0,1,2], 3))

    # print(search([2,5,6,0,0,1,2], 0))
    # print(search([2,5,6,0,0,1,2], 1))
    # print(search([2,5,6,0,0,1,2], 2))
    # print(search([2,5,6,0,0,1,2], 5))
    # print(search([2,5,6,0,0,1,2], 6))
    # print(search([2,5,6,0,0,1,2], 7))
    # print(search([2,5,6,0,0,1,2], 3))
    # print(search([2,5,6,0,0,1,2], 10))
    # print(search([2,5,6,0,0,1,2], -1))
