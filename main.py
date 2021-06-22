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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    from collections import deque
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        queue = deque()
        
        self.increasingBSTHelper(root, queue)

        res = self.increasingBSTBuilder(queue)
        
        return res
        
        
    def increasingBSTHelper(self, root, queue):
        
        if root == None:
            return
        
        if root.left:
            self.increasingBSTHelper(root.left, queue)
            
        queue.append(root.val)
        
        if root.right:
            self.increasingBSTHelper(root.right, queue)
            
            
    def increasingBSTBuilder(self, queue):
        
        currNode = TreeNode(queue[0])
        
        res = currNode
        
        for i in range(len(queue)):
            if i != 0:
                res.right = TreeNode(queue[i])
                res = res.right
                
        return currNode

# ===============

class Solution:
    
    res = 0
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        startingPoint = self.findStartingPoint(grid)
        self.uniquePathsHelper(grid, startingPoint[0], startingPoint[1])
        return self.res        
        
    def uniquePathsHelper(self, grid, x, y):
        width, height = len(grid[0]), len(grid)
        if x < 0 or y < 0 or x >= width or y >= height or grid[y][x] == -1:
            return
        
        if grid[y][x] == 2:
            for i in range(height):
                for j in range(width):
                    if grid[i][j] == 0:
                        return
            self.res += 1
            return
        
        grid[y][x] = -1
        self.uniquePathsHelper(grid, x - 1, y)
        self.uniquePathsHelper(grid, x + 1, y)
        self.uniquePathsHelper(grid, x, y - 1)
        self.uniquePathsHelper(grid, x, y + 1)
        grid[y][x] = 0
        
        
        
    def findStartingPoint(self, grid):
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    return (x, y)

# ===============

