# https://leetcode.cn/problems/minimum-path-sum/submissions/

from typing import List


def minPathSum(grid: List[List[int]]) -> int:
    w=len(grid[0]); h=len(grid)
    dp=[ [
        9999 if i==h or j==w else 0
        for j in range(w+1)
    ] for i in range(h+1) ]     # 这里将 dp 的宽高多加一列，并且将最后一行一列全部置为 9999，避免访问越界到错误的数据

    for i in range(h):
        for j in range(w):
            if i == 0 and j ==0: dp[0][0]=grid[0][0]; continue
            dp[i][j]=min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[-2][-2]


if __name__ == '__main__':
    print(minPathSum([
        [1,3,1],
        [1,5,1],
        [4,2,1],
    ]))
    print(minPathSum([
        [1,2,3],
        [4,5,6]
    ]))
