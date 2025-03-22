class Solution:
    def isValid(self, s):
        par = {')' : '(', ']' : '[', '}' : '{'}
        stack = []

        for i in s:
            if i in par and stack:
                if stack[-1] == par[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        if not stack:
            return True
        return False