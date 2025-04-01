class Solution:
    def generateParenthesis(self, n):
        stack = []
        res = []

        def backtrack(openN, closedN):
            #OpenN = ClosedN = n
            if openN == closedN == n:
                res.append("".join(stack))
                return

            #OpenN <= n:
            if openN <= n:
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop()

            #ClosedN < OpenN:
            if closedN < openN:
                stack.append(')')
                backtrack(openN, closedN + 1)
                stack.pop()
            
        backtrack(0, 0)
        return res
    

#BACKTRACKING IS USED.
#WHAT IS BACKTRACKING?
#
#DO SOMETHING
#SEE IF IT'S RIGHT'
#'IF YES, ADD IT TO YOUR RESULT'
#'IF NOT, GO BACK AND EXPLORE MORE THINGS