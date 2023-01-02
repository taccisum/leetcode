from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    """
    回溯法
    """
    nums = [i+1 for i in range(n)]

    def backt(level):
        if len(sel) == k: res.append(sel.copy()); return    # 选中的数字足够了，将当前组合加入到 res 中
        for i in range(level, len(nums)):
            sel.append(nums[i])     # 选中当前的数字
            backt(i+1)      # 继续下一 level 的 backtracking
            sel.pop()       # 恢复选择状态

    # select 代表选中的元素，res 表示结果
    sel=[]; res=[]; backt(0); return res


if __name__ == '__main__':
    print(combine(4, 2))
    print(combine(1, 1))
