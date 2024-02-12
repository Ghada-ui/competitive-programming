class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        if num%3 == 0 :
            return [num/3 -1, num/3, num/3 +1]   
        return []
        
#         for i in range(num/3,num/2):
#             if (i-2+i-1+i) == num :
#                 return [i-2,i-1,i]    
#         return []
            