class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels={'a','u','i','o','e'}
        ans=[]
        n = len(words)
        vowel_starts = [0] * (n + 1) 
        
        for i in range(n):
            if words[i][0] in vowels and words[i][-1] in vowels:
                vowel_starts[i + 1] = vowel_starts[i] + 1
            else:
                vowel_starts[i + 1] = vowel_starts[i]
        
        for l, r in queries:
            count = vowel_starts[r + 1] - vowel_starts[l]
            ans.append(count)
        
        return ans
                
                