# https://leetcode.cn/problems/delete-operation-for-two-strings/


from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        初始化 m+1 * n+1 二维数组，其中 dp[i][j] 代表 text1 前 i 个字符与 text2 前 j 个字符的最长公共子串长度
        """
        w=len(text1)+1; h=len(text2)+1
        dp = [ [0]*w for i in range(h) ]

        for i in range(1, h):
            for j in range(1, w):
                try:
                    if text2[i-1] == text1[j-1]:
                        """
                        当 text1[i] 与 text2[j] 相同时，状态转移方程为 dp[i][j] = dp[i-1][j-1] + 1
                        例如 'leetc' 与 'etc', 末尾的 c 相同，因此其最大公共子序列长度为 'leet' 与 'et' 的最长公司子序列长度 + 1
                        """
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        """
                        当 text1[i] 与 text2[j] 不相同时，状态转移方程为 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                        例如 'leetco' 与 'etc', 末尾的字符 c 和 o 不相同，因此其最大公共子序列长度要么是 'leetc' 与 'etc' 的最长公共子序列长度，要么是 'leetco' 与 'et' 的最长公共子序列长度
                        """
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                except:
                    print('err', i, j)
        
        return dp[-1][-1]


if __name__ == '__main__':
    s=Solution()
    assert s.longestCommonSubsequence('hello', 'world') == 1
    assert s.longestCommonSubsequence('leetcode', 'etco') == 4
    assert s.longestCommonSubsequence('a', 'a') == 0
