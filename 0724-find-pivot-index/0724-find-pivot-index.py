class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        accum = 0
        accum1 = 0
        prefix_sum_left = []
        prefix_sum_right = []
        for i in range(len(nums)):
            prefix_sum_left.append(accum)
            accum += nums[i]
        for j in range(len(nums)-1,-1,-1):
            prefix_sum_right.append(accum1)
            accum1 += nums[j] 
        prefix_sum_right.reverse()
        for k in range(len(prefix_sum_left)):
            if prefix_sum_left[k] == prefix_sum_right[k]:
                return k
        return -1    
        
            
            
        