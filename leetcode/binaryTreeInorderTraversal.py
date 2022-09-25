# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Method: Depth-First-Search(recursion)
    Time complexity: O(n), given that n is the numbers of nodes
    Space complexity: O(n), given that n is the numbers of nodes
    '''
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret_list = []
        
        # if the given list is empty
        if not root:
            return
        
        if root.left:
            ret_list += self.inorderTraversal(root.left)
            
        ret_list.append(root.val)
        
        if root.right:
            ret_list += self.inorderTraversal(root.right)
        
        return ret_list

    