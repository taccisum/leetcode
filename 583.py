# https://leetcode.cn/problems/delete-operation-for-two-strings/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w=len(word1)+1; h=len(word2)+1
        dp = [ [0]*w for i in range(h) ]

        for i in range(1, h):
            for j in range(1, w):
                try:
                    if word2[i-1] == word1[j-1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                except:
                    print('err', i, j)
        
        max_csl = dp[-1][-1]    # 这里先求出最长公共子序列 Max Common Subsequence Length
        return (len(word1) - max_csl) + (len(word2) - max_csl)      # 需要删除的字符数，即是原字段串与公共子序列的长度差


if __name__ == '__main__':
    s=Solution()
    print(s.minDistance('hello', 'world'))
    assert s.minDistance('hello', 'world') == 8
    assert s.minDistance('leetcode', 'etco') == 4
    assert s.minDistance('a', 'a') == 0
