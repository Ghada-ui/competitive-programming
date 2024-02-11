class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list_negative=[]
        list_positive=[]
        result=[]
        for i in range (len(nums)):
            if nums[i]<0:
                list_negative.append(nums[i])
            else:
                list_positive.append(nums[i])
        for i1,i2 in zip(list_positive,list_negative):
            result.append(i1)
            result.append(i2)
        return result    