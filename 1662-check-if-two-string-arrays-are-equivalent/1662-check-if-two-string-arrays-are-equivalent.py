class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        wd1=""
        wd2=""
        for i in range(len(word1)):
            wd1=wd1+word1[i]
        for i in range(len(word2)):
            wd2=wd2+word2[i]    
        if wd1==wd2:
            return True
        else:
            return False