class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        frequency = Counter(nums)
        max_freq_elements = []

        for key, value in frequency.items():
            if value > (len(nums)/3):
                max_freq_elements.append(key)
        return max_freq_elements
            