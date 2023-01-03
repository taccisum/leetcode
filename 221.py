# https://leetcode.cn/problems/maximal-square/

from cmath import sqrt
from typing import List

def _print(arr2d):
    for i in range(len(arr2d)):
        for j in range(len(arr2d[0])):
            print(arr2d[i][j], end='\0')
        print()

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        dp[i][j] 表示到 [i,j] 从当前点往左上方延伸能构成的最大的正方形长度
        对于任一正方形
        1 1 1
        1 1 1
        1 1 1
        有对应 dp 数组
        1 1 1
        1 2 2
        1 2 3

        特殊情况：[2,2] 左边和上边两个 2*2 的正方形重叠
        0 1 1
        1 1 1
        1 1 1
        对应 dp 数组，此时 dp[2][2] 应为 dp[1][1]+1
        0 1 1
        1 1 2
        1 2 2
        """

        w=len(matrix[0]); h=len(matrix)
        dp=[ [ 0 for j in range(w+1) ] for i in range(h+1) ]     # 这里将 dp 的宽高多加一列，并且将最后一行一列全部置为 9999，避免访问越界到错误的数据

        dp[0][0] = int(matrix[0][0]); max_=dp[0][0]
        for i in range(h):
            for j in range(w):
                if i == 0 and j == 0: continue
                if matrix[i][j] == '1':
                    dp[i][j]=min(dp[i-1][j], min(dp[i][j-1], dp[i-1][j-1]))+1   # 状态转移方程
                    max_=max(max_, dp[i][j])
        
        # _print(dp)
        return max_**2


if __name__ == '__main__':
    s=Solution()
    assert s.maximalSquare([
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]) == 4
    assert s.maximalSquare([['1']]) == 1
    assert s.maximalSquare([
        ["1","0","1","0"],
        ["1","0","1","1"],
        ["1","0","1","1"],
        ["1","1","1","1"]
    ]) == 4
    assert s.maximalSquare([
        ["1","0","1","0","0","1","1","1","0"],
        ["1","1","1","0","0","0","0","0","1"],
        ["0","0","1","1","0","0","0","1","1"],
        ["0","1","1","0","0","1","0","0","1"],
        ["1","1","0","1","1","0","0","1","0"],
        ["0","1","1","1","1","1","1","0","1"],
        ["1","0","1","1","1","0","0","1","0"],
        ["1","1","1","0","1","0","0","0","1"],
        ["0","1","1","1","1","0","0","1","0"],
        ["1","0","0","1","1","1","0","0","0"]
    ]) == 4
    assert s.maximalSquare([
        ["0","1","1","0","1"],
        ["1","1","0","1","0"],
        ["0","1","1","1","0"],
        ["1","1","1","1","0"],
        ["1","1","1","1","1"],
        ["0","0","0","0","0"]
    ]) == 9
