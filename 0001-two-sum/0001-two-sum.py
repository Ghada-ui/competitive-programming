class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result =[]
        my_dict={}
        for i in range (len(nums)):
            if (target - nums[i]) in my_dict: 
                result.append(i)
                result.append(my_dict[target - nums[i]])
                break
            my_dict[nums[i]]= i    
        return result        
                
        