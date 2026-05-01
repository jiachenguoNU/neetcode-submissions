# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #这个很基础，就是最简单的level traversal定义
        #注意这里list是append list，而不是extend

        if not root:
            return []
        
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            level_list = []
            num_nodes_this_level = len(queue)
            for _ in range(num_nodes_this_level):
                node = queue.popleft()
                level_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_list)
        return res
