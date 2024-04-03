class Solution:    
    def longestBeautifulSubstring(self, word: str) -> int:
        left = 0
        result = 0
        sub_array=Counter(word[0])
        
        for right in range(1,len(word)):
            if word[right-1]<=word[right]:
                sub_array[word[right]]+=1
                if len(sub_array)==5:
                    result=max(result,right-left+1)
            else:
                sub_array=Counter()
                left = right
                sub_array[word[right]]+=1
        return result     
                    
        
                
            
            