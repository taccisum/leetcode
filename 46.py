from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    """
    回溯法，直接修改原数组状态，并在递归完成后恢复，可以避免重复创建数组的 copy 导致浪费空间
    """

    def swap(nums, a, b):
        if a != b: tmp = nums[a]; nums[a] = nums[b]; nums[b] = tmp

    def backt(nums:List[int], level, res:List[List[int]]):
        if level+1 >= len(nums): res.append(nums.copy()); return    # 检索到末端了，将这个组合加入 result

        for i in range(level, len(nums)):
            swap(nums, level, i)    # 修改状态
            backt(nums, level+1, res)
            swap(nums, level, i)    # 恢复状态，准备进行下一次遍历

    # 虚拟一个根节点并对 nums 启动 backtracking，将结果记录到 res 中
    res = []; backt(nums, 0, res); return res


if __name__ == '__main__':
    print(permute([1,2,3]))     # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(permute([3,5,8,10]))

    