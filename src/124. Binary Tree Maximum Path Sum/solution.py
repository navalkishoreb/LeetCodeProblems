# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# input  output
#[-3] --> -3
#[2,-1] --> 2
#[1,-2,3] --> 4
#1,-2,-3,1,3,-2,null,-1] -> 3
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]


        def dfs(root):
            if root == None:
                return 0
            
            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right), 0)
            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)
            
        dfs(root)
        return res[0]

