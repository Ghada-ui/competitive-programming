class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = s.split()
        stringres=""
        for i in reversed(result):
            if i != result[len(result)-1]:    
                stringres=stringres+" "+i 
            else:
                stringres=stringres+i 
        return stringres
        