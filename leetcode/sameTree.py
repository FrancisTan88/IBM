

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Method: Naive(recursion)
    Time complexity: O(n), given that n is the number of the nodes
    Space complexity: O(n) in the worst case of completely unbalanced tree, to keep a recursion stack.
    '''
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (p and not q) or (not p and q):
            return False
        if p.val != q.val:
            return False
        
        # p.val == q.val
        else:
            return self.isSameTree(p.left, q.left) and \
                self.isSameTree(p.right, q.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and not q:
            return False
        elif not p and q:
            return False
        elif not p and not q:
            return True
        elif p.val != q.val:
            return False
        elif p.val == q.val:
            if not self.isSameTree(p.left, q.left): return False
            if not self.isSameTree(p.right, q.right): return False
            return True