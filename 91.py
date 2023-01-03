# https://leetcode.cn/problems/decode-ways/


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0': return 0

        dp=[1 for i in range(len(s))]

        for i in range(1, len(s)):
            c=s[i]; pc=s[i-1]
            c_ascii=ord(c); pc_ascii=ord(pc)

            if c_ascii==ord('0'):
                if pc_ascii>ord('2') or pc_ascii==ord('0'): return 0   # 当前数字为 0，且无法与前数字组合，则直接返回 0
                else:
                    # 如果前面的数字小于 2，那必然要跟这个 0 组合，所以数量跟 dp[i-2] 是一样的，此时的状态转移方程为
                    dp[i]=dp[i-2]
            elif pc_ascii==ord('1') or (pc_ascii==ord('2') and c_ascii<=ord('6')):
                # 当前数字不为 0 且可以和前数字构成字母，此时的状态转移方程为
                dp[i]=dp[i-2]+dp[i-1]
            else:
                dp[i]=dp[i-1]       # 如果条件都不符合，则使用这个状态转移方程

        # print(dp)
        return dp[len(s)-1]


if __name__ == '__main__':
    s=Solution()
    # 11233333  <- 对应 dp
    # 51238757  <- 输入
    assert s.numDecodings('5') == 1
    assert s.numDecodings('51') == 1
    assert s.numDecodings('512') == 2
    assert s.numDecodings('5123') == 3
    assert s.numDecodings('51238') == 3
    assert s.numDecodings('12') == 2
    assert s.numDecodings('226') == 3
    assert s.numDecodings('06') == 0
    assert s.numDecodings('606') == 0
    assert s.numDecodings('206') == 1
    assert s.numDecodings('10011') == 0
    assert s.numDecodings('2611055971756562') == 4
    assert s.numDecodings('11106') == 2
    print(s.numDecodings('51238757'))
