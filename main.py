# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        
        res = 0
        traversalList = []
        self.rangeSumBSTHelper(root, low, high, traversalList)
        for i in traversalList:
            if low <= i <= high:
                res += i
                
        return res
        
        
    def rangeSumBSTHelper(self, root, low, high, traversalList):        
        
        if root == None:
            return res       
        
        if root.left:
            self.rangeSumBSTHelper(root.left, low, high, traversalList)
        
        traversalList.append(root.val)
        
        if root.right:
            self.rangeSumBSTHelper(root.right, low, high, traversalList)

# ===============

