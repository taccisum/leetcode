# https://leetcode.cn/problems/number-of-provinces/

from typing import List


def findCircleNum(isConnected: List[List[int]]) -> int:
    width=len(isConnected[0]); height=len(isConnected)        # 计算长宽

    c=0; stack=[];
    for i in range(height):
        for j in range(width):
            if isConnected[i][j] == 1:
                # 开始 dfs
                clear=set()
                stack.append(i)     # 第 i 个人入栈
                while len(stack) > 0:
                    x = stack.pop(); y = j
                    if x in clear: continue
                    while y < width:
                        if isConnected[x][y] == 1:
                            isConnected[x][y] = 0
                            if x != y and x not in clear: stack.append(y)
                        y+=1
                    clear.add(x)     # 记忆已经检索过的行，提高性能
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
