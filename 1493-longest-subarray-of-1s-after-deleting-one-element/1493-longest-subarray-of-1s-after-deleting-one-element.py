class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        result = Counter()
        resultat = 0
        
        for right in range(len(nums)):
            result[nums[right]]+=1
            while result[0]>1:
                result[nums[left]]-=1
                if result[nums[left]] == 0:
                    del result[nums[left]]
                left+=1
            resultat = max(resultat,right-left+1)
        return resultat-1   
                
                
            