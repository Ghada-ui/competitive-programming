class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) <= 0 :
            return ""
         
        result = strs[0]
        for i in range(1, len(strs)):
            if len(result) == 0 :
                return result
            
            j = 0
            while result[:j] == strs[i][:j] and j <= len(result):
                j += 1
                
            result = result[:j-1]

        return result