class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target :
                return i
            elif target < nums[i]:
                return i
            elif target > nums[len(nums)-1]:
                return (len(nums))