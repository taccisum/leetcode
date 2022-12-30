# https://leetcode.cn/problems/max-area-of-island/

from typing import List

def safe_direction4(i, j, height, width):
    """
    返回上下左右四个方向的坐标（自动剔除越界坐标）
    """
    d=[]
    if i > 0: d.append((i-1, j))    # up i-1, j
    if i < height-1: d.append((i+1, j))     # down i+1, j
    if j > 0: d.append((i, j-1))    # left i, j-1
    if j < width-1: d.append((i, j+1))      # right i, j+1
    return d

def maxAreaOfIslandStackEdition(grid: List[List[int]]) -> int:
    """
    Stack 版本
    """
    width=len(grid[0]); height=len(grid)        # 计算 grid 长宽

    max_area=0; stack=[]
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                stack.append((i, j)); partial_area=0        # 找到一个不为 0 的节点，开始 dfs
                while len(stack) > 0:
                    x0, y0 = stack.pop()
                    if (grid[x0][y0]) == 0: continue        # 这里要再进行一次判断，因为这个节点可能在别的 dfs 分支中已经处理过了
                    grid[x0][y0]=0; partial_area+=1    # 将起点置 0，避免重复搜索，同时统计 area 面积加 1
                    for x, y in safe_direction4(x0, y0, height, width):
                        if grid[x][y] == 1: stack.append((x, y))

                max_area = max(max_area, partial_area)
    return max_area



def maxAreaOfIslandRecursively(grid: List[List[int]]) -> int:
    """
    递归版本，空间和时间复杂度都相对较高，且有 Stackoverflow 的风险
    """
    width=len(grid[0]); height=len(grid)        # 计算 grid 长宽

    def dfs(grid: List[List[int]], i, j):
        """
        dfs 辅助函数
        """
        if grid[i][j] == 0: return 0
        grid[i][j]=0; area=1    # 将起点置 0，避免重复搜索
        for x, y in safe_direction4(i, j, height, width):
            if grid[x][y] == 1:
                area += dfs(grid, x, y)
        return area

    max_area=0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                max_area = max(max_area, dfs(grid, i, j))
    return max_area


if __name__ == '__main__':
    # maxAreaOfIsland=maxAreaOfIslandRecursively
    maxAreaOfIsland=maxAreaOfIslandStackEdition
    print(safe_direction4(0, 1, 2, 2))
    print(safe_direction4(1, 1, 2, 2))
    from copy import deepcopy
    area = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    assert maxAreaOfIsland(deepcopy(area)) == 6
    print(maxAreaOfIsland(deepcopy(area)))    # print 6
    area1 = [
        [1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,1,1],
        [0,0,0,1,1]
    ]
    assert maxAreaOfIsland(deepcopy(area1)) == 4
    assert maxAreaOfIsland([[0,1],[1,1]]) == 3
    
    # print(dfs(area, 0, 7))      # print 4
