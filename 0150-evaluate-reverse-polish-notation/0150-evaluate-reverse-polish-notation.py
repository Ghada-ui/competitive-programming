class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if token == '+' :
                    result = num1 + num2 
                if token == '-' :
                    result = num1 - num2 
                if token == '*':
                    result = num1 * num2 
                if token == '/' :
                    result = num1 / num2     
                    
                stack.append(result)               
            else:
                stack.append(token)
        return int(stack[0])
       
        