class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        stack = []
        def backtrack(openCount, closedCount):
            if openCount == closedCount == n:
                res.append("".join(stack))
                return
            
            if openCount < n:
                stack.append("(")
                backtrack(openCount + 1, closedCount)
                stack.pop()
            
            if closedCount < openCount:
                stack.append(")")
                backtrack(openCount, closedCount + 1)
                stack.pop()
        

        backtrack(0,0)
        return res
