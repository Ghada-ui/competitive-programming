class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        result=""
        for i in range (len(command)):
            if command[i]=="G":
                result = result + 'G'
            elif command[i]=='('and command[i+1]==')':
                result = result + 'o'
            elif command[i]=='(' and command[i+1]=='a':
                result = result + 'al'
            else:
                i=i+1
        return result       
                