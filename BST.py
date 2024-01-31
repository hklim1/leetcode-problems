# === TOTALS ===
# EASY: 

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

# PROBLEM 100: SAME TREE (EASY) - JANUARY 22, 2024
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if (p == None and q != None) or (p != None and q == None):
            return False
        if p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        if left == True and right == True and p.val == q.val:
            return True
        else:
            return False

# PROBLEM 144: BINARY TREE PREORDER TRAVERSAL (EASY) - JANUARY 18, 2024
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer_array = []
        if root == None:
            return answer_array
        answer_array.append(root.val)
        left_val = self.preorderTraversal(root.left)
        right_val = self.preorderTraversal(root.right)
        return answer_array + left_val + right_val

# PROBLEM 145: BINARY TREE POSTORDER TRAVERSAL (EASY) - JANUARY 18, 2024
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer_array = []
        if root == None:
            return answer_array
        answer_array.append(root.val)
        left_val = self.postorderTraversal(root.left)
        right_val = self.postorderTraversal(root.right)
        return left_val + right_val + answer_array

# PROBLEM 94: BINARY TREE INORDER TRAVERSAL (EASY) - JANUARY 17, 2024
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer_array = []
        if root == None:
            return []
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        answer_array += left
        answer_array.append(root.val)
        answer_array += right
        return answer_array