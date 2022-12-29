from math import floor


def find_min(nums):
    def min_(a, b):
        return a if a <= b else b

    l=0; r=len(nums)

    # 处理边界条件
    if r == 0: return None
    if r == 1: return nums[0]

    # 初始值设为比可能出现的最大值大即可（leetcode 用例条件之一为：-5000 <= nums[i] <= 5000）
    min = 9999
    while l < r:
        mid = floor((l+r)/2)
        min = min_(nums[mid], min)      # 取中间值和当前最小值中较小的

        # 无法判断是否有序
        if nums[mid] == nums[l]:
            l+=1; continue
        elif nums[mid] == nums[r-1]:
            r-=1; continue
        
        if nums[mid] > nums[l]:
            # 左边有序，比较并更新最小值
            min = min_(nums[l], min)
            # 继续在右边找是否有更小值
            l=mid
        else:
            # 右边有序，继续在左边找是否有更小值
            r=mid

    return min


if __name__ == '__main__':
    print(find_min([2,2,2,0,1]))       # print 0
    print(find_min([1,3,5]))       # print 1

    # leetcode 特殊用例
    print(find_min([1]))       # print 1
    print(find_min([1,1]))       # print 1