# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #base case
        if not preorder:
            return None
        
        #pre-order traversal
        curr_node = preorder[0]
        root = TreeNode(curr_node)
        node_idx = inorder.index(curr_node)
        #in order tree split
        left_inorder = inorder[:node_idx]
        right_inorder = inorder[node_idx + 1:]

        #pre-order tree split [this part needs thinking]
        left_preorder = preorder[1:node_idx + 1] #why 1:mid+1
        right_preorder = preorder[node_idx + 1:]
        #left_tree
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        #right_tree

        return root