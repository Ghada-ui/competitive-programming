class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for k in range(1, rowIndex + 1):
            element_k = row[k - 1] * (rowIndex - k + 1) // k
            row.append(element_k)  
        return row
        