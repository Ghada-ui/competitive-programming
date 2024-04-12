class NumArray:

    def __init__(self, nums: List[int]):
        prefix_sum = []
        pr = 0
        for i in range(len(nums)):
            pr += nums[i]
            prefix_sum.append(pr)
        prefix_sum.append(0)
        self.prefix_sum = prefix_sum    

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right] - self.prefix_sum[left-1]  
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)