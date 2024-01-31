# PROBLEM 2331 EVALUATE BOOLEAN BINARY TREE (EASY) - JANUARY 31, 2024
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == 1:
            return True
        if root.val == 0:
            return False

        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)

        if root.val == 2:
            return left or right
        elif root.val == 3:
            return left and right
        else:
            return False

# PROBLEM 104: MAXIMUM DEPTH OF BINARY TREE (EASY) - JANUARY 30, 2024
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        if left >= right:
            return 1 + left

        if right > left:
            return 1 + right