class Solution:
    def evalRPN(self, tokens):
        stack = []
        expressions = {'+', '-', '/', '*'}

        for i in range(len(tokens)):
            if tokens[i] not in expressions:
                stack.append(int(tokens[i]))
            else:
                a = stack.pop()
                b = stack.pop()
            
                if tokens[i] == '+':
                    ans = a + b

                elif tokens[i] == '-':
                    ans = b - a

                elif tokens[i] == '*':
                    ans = a * b

                else:
                    ans = int(b / a)
                
                stack.append(ans)

        return stack[-1]