class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def findMaxIndex(arr, n):
            max_index = 0
            for i in range(1, n):
                if arr[i] > arr[max_index]:
                    max_index = i
            return max_index
        
        def flip(arr, k):
            left, right = 0, k - 1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        
        result = []
        n = len(arr)
        
        while n > 1:
            max_index = findMaxIndex(arr, n)
            
            if max_index != n - 1:
                if max_index != 0:
                    flip(arr, max_index + 1)
                    result.append(max_index + 1)
                
                flip(arr, n)
                result.append(n)
            
            n -= 1
        
        return result
