# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #post order traversal: max gain from the downward subtrees
        #accumulation nonlocal max_val
        max_sum = float("-inf")

        def dfs(node):
            if not node:
                return 0
            nonlocal max_sum

            max_left_downward = max(dfs(node.left), 0)
            max_right_downward = max(dfs(node.right), 0)

            max_sum_downward = node.val + max(max_left_downward, max_right_downward)
            curr_max_sum = node.val + max_left_downward + max_right_downward
            max_sum = max(curr_max_sum, max_sum)

            #这里必须要return：当下node作为子问题时的max_sum
            return max_sum_downward

        dfs(root)
        return max_sum



        