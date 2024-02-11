class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        mylist_right=[]
        mylist_left=[]
        mylist_middle=[]
        
        for i in range(len(nums)):
            if nums[i]<pivot:
                mylist_left.append(nums[i])
            elif nums[i]==pivot:
                mylist_middle.append(nums[i])
            elif nums[i]>pivot:
                mylist_right.append(nums[i])
        return mylist_left+mylist_middle+mylist_right
        