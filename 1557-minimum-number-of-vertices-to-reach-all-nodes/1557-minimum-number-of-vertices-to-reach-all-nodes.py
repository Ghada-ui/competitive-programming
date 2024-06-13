class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [True for i in range(n)]
        for u, v in edges: 
            adj [v] = False
        ans = []
        for i in range(n):
            if adj[i]:
                ans.append(i)
        return ans
        