class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        for i in range(len(nums)):
            small = 0
            for j in range(len(nums)):
                if nums[j]<nums[i] and j != i:
                    small+=1
            result.append(small)  
        return result    