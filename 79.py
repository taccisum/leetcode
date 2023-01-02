# https://leetcode.cn/problems/word-search/submissions/

from typing import List

from common import *


def exist(board: List[List[str]], word: str) -> bool:
    """
    回溯法(性能较差, leetcode 执行需要接近 6s, 仅前 22%)
    """
    width=len(board[0]); height=len(board)
    visited=[[False for j in range(width)] for i in range(height)]      # 标记是否已访问过目标元素

    def backt(x0, y0, level):
        # print('[%d, %d]' % (x0, y0), level)
        if board[x0][y0] != word[level]: return False
        if level >= len(word)-1: return True

        visited[x0][y0] = True        # 标识为已访问
        for x, y in safe_direction4(x0, y0, height, width):
            if not visited[x][y]:
                if backt(x, y, level+1): return True       # 如果匹配成功，直接中止回溯
        visited[x0][y0] = False       # 【回溯】恢复访问标识
        return False    # 四个方向的分支全部匹配失败了，则返回 Flase

    for i in range(height):
        for j in range(width):
            # print('start backtracing from root: [%d, %d]' %(i, j))
            if backt(i, j, 0): return True
    return False


if __name__ == '__main__':
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    print(exist(board, 'ABCCED'))     # print True
    print(exist(board, 'ABCCEDFF'))     # print False
    print(exist(board, 'ABCCCCCCCC'))     # print False

    # leetcode 特殊用例
    print(exist([
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ], 'SEE'))     # print True
    print(exist([['a']], 'b'))     # print False
    print(exist([['a','a']], 'aaa'))     # print False
    print(exist([['a','a']], 'aaa'))     # print False
    print(exist([
        ["A","A","A","A","A","A"],
        ["A","A","A","A","A","A"],
        ["A","A","A","A","A","A"],
        ["A","A","A","A","A","A"],
        ["A","A","A","A","A","A"],
        ["A","A","A","A","A","A"]
    ], 'BAAAAAAAAAAAAAA'))     # print False