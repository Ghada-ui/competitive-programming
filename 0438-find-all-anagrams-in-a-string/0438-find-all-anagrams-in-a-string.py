class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counter=Counter(p)
        p_length = len(p)
        s_counter=Counter(s[:p_length])
        result=[]
        if p_counter == s_counter:
            result.append(0)
        left = 0
        
        for right in range(p_length,len(s)):
            s_counter[s[right]] += 1
            s_counter[s[left]] -= 1
            if s_counter[s[left]] == 0:
                s_counter.pop(s[left])
            left+=1
            if p_counter == s_counter:
                result.append(left)
                
        return result       
            
            
            
        
        
        