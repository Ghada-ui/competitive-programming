class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        r=int(''.join(map(str, digits)))+1  
        my_list = [int(digit) for digit in str(r)]
        return my_list    