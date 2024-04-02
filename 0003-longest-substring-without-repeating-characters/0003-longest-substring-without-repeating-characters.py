class Solution(object):
    
    def isUnique(self,chaine):
        seen = set()
        for char in chaine:
            if char in seen:
                return False
            seen.add(char)
        return True 

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        chaine=""
        n = len(s)
        left = 0
        right=0
        while right < n:
            if self.isUnique(s[left:right+1]):
                result = max(result, right - left + 1)
                right += 1
            else:
                left += 1  
        return result        
                
            
            
