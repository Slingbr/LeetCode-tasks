"""
 Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

Examples:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Note: "pwke" is a subsequence, not a substring.
"""

"""my brute force solution"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        highest_len = 0

  n = len(s)
        
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
                highest_len = max(highest_len, j - i + 1)
        
        return highest_len
sol = Solution()
input_str = "abcabcbb"
result = sol.lengthOfLongestSubstring(input_str)
print("Output:", result)
