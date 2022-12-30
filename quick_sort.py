def quick_sort(nums):
    def sort(nums, l, r):
        if l + 1 >= r: return       # 要处理的元素已经小于等于 1，直接返回
        first=l; last=r-1; pivot=nums[first]

        while first < last:
            # 循环结束条件为 first 与 last 相遇
            while first < last and nums[last] >= pivot:
                # 从右边找到下一个比 pivot 小的元素
                last-=1
            nums[first]=nums[last]        # first 此时为 pivot，直接将 last 值覆盖 first 即可
            while first < last and nums[first] <= pivot:
                # 从左边找到下一个比 pivot 大的元素
                first+=1
            nums[last]=nums[first]        # last 此时为 pivot，直接将 first 值覆盖 last 即可
        
        # 结束后应该将相遇位置值置为 pivot
        nums[first]=pivot

        # 继续展开下一轮排序
        # 由于这轮排序已经确定的是 pivot 位置一定是对的，因此下一轮排序无需将其包括进来也可以
        # 这里左区间是 [l, pivot)，右区间是 [pivot+1, r]
        sort(nums, l, first)
        sort(nums, first+1, r)

    sort(nums, 0, len(nums))        # 左闭右开原则
    return nums


def quick_sort0(nums):
    def swap(nums, a, b):
        if a == b: return
        print('swap', a, b)
        tmp = nums[a]
        nums[a] = nums[b]
        nums[b] = tmp

    def sort(nums, s, e):
        print('sort', s, e)
        l=s; r=e-1; pivot=s; flag=False

        if e-s < 2: return
        if e-s == 2 and nums[e-1] < nums[s]:
            swap(nums, s, e-1)
            
        while l < r - 1:
            if flag:
                # 从左边找一个比 pivot 大的
                while nums[l] <= nums[pivot]:
                    l+=1
                    if l>=pivot: break
                if l<pivot:
                    swap(nums, l, pivot)
                    pivot=l
            else:
                # 从右边找一个比 pivot 小的
                while nums[r] >= nums[pivot]:
                    r-=1
                    if r<=pivot: break
                if r>pivot:
                    swap(nums, pivot, r)
                    pivot=r

            flag=not flag
        

        if pivot == l:
            # pivot 等于 l，说明 pivot 是最小的数，避免死循环将 pivot 右移一位
            pivot += 1

        sort(nums, s, pivot)
        sort(nums, pivot, e)
    
    sort(nums, 0, len(nums))
    return nums


if __name__ == '__main__':
    print(quick_sort([20,7,35,17,66,25,3,27]))
    # print(quick_sort([6,1,2,4,6,2,7]))
    # [*6,1,2,4,6,2,7]
    # [2,1,2,4,6,*6,7]
    # [2,1,2,4,*6,6,7]
    # [*2,1,2,4][*6,6,7]
    # [1,*2,2,4][*6,6,7]

    # print(quick_sort([2,1,2,4,6]))
    # print(quick_sort([1]))
    # print(quick_sort([2,2,4,6]))
    # print(quick_sort([1,2,4,6]))
    # print(quick_sort([2,1,2,4]))
    # print(quick_sort([6,6,7]))
    # print(quick_sort([6,1,2,4]))
