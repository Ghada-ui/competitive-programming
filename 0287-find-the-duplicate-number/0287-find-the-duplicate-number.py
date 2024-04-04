class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        binary_representations = {}
        for num in nums:
            if (bin(num)) in binary_representations: 
                return num
                break
            binary_representations[bin(num)]= bin(num)    
        