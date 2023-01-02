# https://leetcode.cn/problems/01-matrix/

from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        w=len(mat[0]); h=len(mat)
        dp=[ [
            9999 if i==h or j==w else 0
            for j in range(w+1)
        ] for i in range(h+1) ]     # 这里将 dp 的宽高多加一列，并且将最后一行一列全部置为 9999，避免访问越界到错误的数据
        res=[ [ 0 for j in range(w) ] for i in range(h) ]

        # 这里是不需要预处理最左上角的数据的，如果左上角是以 1 开始，只需要把它置为一个特别大的数来代表未知值就好了
        for i in range(h):
            for j in range(w):
                if mat[i][j] == 0: continue
                min_=min(dp[i-1][j], dp[i][j-1]) + 1    # 状态转移方程
                res[i][j]=min_; dp[i][j]=min_

        # 从右下角到左上角再遍历一次，目的有二：1. 处理第一次遍历无法处理的未知值 2. 比较两个方向访问产生的不同距离，取较小的一个
        for i in reversed(range(h)):
            for j in reversed(range(w)):
                if mat[i][j] == 0: continue
                min_=min(
                    dp[i][j],
                    min(dp[i+1][j], dp[i][j+1]) + 1
                )    # 第二次遍历的状态转移方程还要跟第一次的结果进行比较
                res[i][j]=min_; dp[i][j]=min_

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.updateMatrix([
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]))
    print(solution.updateMatrix([
        [0,1,0,1,1],
        [1,1,0,0,1],
        [0,0,0,1,0],
        [1,0,1,1,1],
        [1,0,0,0,1]
    ]))
    print(solution.updateMatrix([
        [0,0,0],
        [0,1,0],
        [1,1,1]
    ]))
    print(solution.updateMatrix([
        [1,1,0,0,1,0,0,1,1,0],
        [1,0,0,1,0,1,1,1,1,1],
        [1,1,1,0,0,1,1,1,1,0],
        [0,1,1,1,0,1,1,1,1,1],
        [0,0,1,1,1,1,1,1,1,0],
        [1,1,1,1,1,1,0,1,1,1],
        [0,1,1,1,1,1,1,0,0,1],
        [1,1,1,1,1,0,0,1,1,1],
        [0,1,0,1,1,0,1,1,1,1],
        [1,1,1,0,1,0,1,1,1,1]]
    ))
