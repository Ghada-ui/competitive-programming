class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_sum = sum(nums[:k])
        max_value = window_sum
        n = len(nums)
        for i in range(n-k):
            window_sum=window_sum - nums[i] + nums[i+k]
            max_value=max(window_sum,max_value)
        return max_value/float(k)    