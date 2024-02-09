class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        winner =[]
        oneloss = []
        dictL={}
        dictW={}
        for match in matches:
            dictL[match[1]] = dictL.get(match[1], 0) + 1
            dictW[match[0]]= dictW.get(match[1], 0) +1
      
        for key, value in dictL.items():
            if value == 1:  
                oneloss.append(key)
        
        for key, value in dictW.items():
            if key not in dictL:
                winner.append(key)
                
        winner.sort()
        oneloss.sort()        
        return [winner, oneloss]    
            
        