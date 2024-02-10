class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        shuffle_list=[]
        for i in range(n):
            shuffle_list.append(nums[i])
            shuffle_list.append(nums[i+n])
        return shuffle_list    

            
            
            