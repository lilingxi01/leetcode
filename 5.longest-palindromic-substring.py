#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        longest = s[0]
        for i in range(len(s)):
            dp[i][i] = True
        for length in range(2, len(s) + 1):
            for start in range(len(s) - length + 1):
                end = start + length - 1
                if s[start] == s[end] and (length == 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    if end - start + 1 > len(longest):
                        longest = s[start:end + 1]
        return longest
# @lc code=end

