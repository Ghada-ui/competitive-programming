class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result=[]
        for row in range(len(mat)):
            mat[row].append(row)
        
        mat.sort()
        print(mat)
        for i in range(k):
            result.append(mat[i][-1])
        return result    
     
        
        