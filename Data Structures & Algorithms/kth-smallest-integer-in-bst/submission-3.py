class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #从这个例子可以发现这里是个global的性质，所以得有个global的list来存储。存储完了然后选？太傻逼了这个方法
        #是不是应该从左下方开始呢？ 这样能最快找到？不对，所有的call都只能从root出发
        #有序链表，指针？
        #右边的数的所有元素总是大于现在的节点
        res_list = []

        def dfs(node, res_list):
            if not node:
                return
            
            if node.left:
                dfs(node.left, res_list)
            res_list.append(node.val)
            if node.right:
                dfs(node.right, res_list)
        dfs(root, res_list)
        return res_list[k-1]