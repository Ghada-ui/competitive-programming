class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        first_row=set("qwertyuiop")
        second_row=set("asdfghjkl")
        third_row=set("zxcvbnm")
        result=[]
        for word in words :
            word_char=set(word.lower())
            if word_char.issubset(first_row)or word_char.issubset(second_row) or word_char.issubset(third_row):
                result.append(word)
        return result        