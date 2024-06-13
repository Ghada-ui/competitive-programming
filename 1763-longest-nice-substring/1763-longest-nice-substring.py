class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        char = set(s)
        if len(s) < 2:
            return ""
        for i, c in enumerate(s):
            if c.swapcase() not in char:
                left = self.longestNiceSubstring(s[0:i])
                right = self.longestNiceSubstring(s[i+1:])
                return right if len(right) > len(left) else left
        return s
        