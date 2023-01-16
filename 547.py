# https://leetcode.cn/problems/number-of-provinces/

from typing import List


def findCircleNum(isConnected: List[List[int]]) -> int:
    width=len(isConnected[0]); height=len(isConnected)        # 计算长宽

    c=0; stack=[]; visited=set()
    for i in range(height):
        for j in range(width):
            if isConnected[i][j] == 1:
                stack.append(i)     # 根节点入栈，开始 dfs
                while len(stack) > 0:
                    x=stack.pop(); y=j      # 直接从 y=j 开始检索
                    if x in visited: continue   # 避免重复遍历
                    visited.add(x)     # 记忆已经检索过的行
                    while y < width:
                        if isConnected[x][y] == 1:
                            isConnected[x][y] = 0   # 将已经访问过的节点置为 0，避免重复访问
                            if x != y: stack.append(y)      # 新的分支节点入栈
                        y+=1
                c+=1
                break
    return c


if __name__ == '__main__':
    friendship = [
        [1,1,0],
        [1,1,0],
        [0,0,1]
    ]
    print(findCircleNum(friendship))        # print 2
