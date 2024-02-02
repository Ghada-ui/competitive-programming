class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        r=0
        for i in range (len(operations)):
            if "++" in operations[i]:
                r = r + 1
            elif "--" in operations[i]: 
                r = r - 1
        return r        