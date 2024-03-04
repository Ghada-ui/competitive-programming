class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set_1=set(nums1)
        set_2=set(nums2)
        intersection = set_1.intersection(set_2)
        result = [num for num in intersection for _ in range(min(nums1.count(num), nums2.count(num)))]
        return result
        