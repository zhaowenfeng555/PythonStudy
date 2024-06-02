# encoding: utf-8
# @author: fengr358
# @time: 2021/5/22 21:41
# @desc:
# 最近公共祖先：
# 思路：dfs遍历，dict存储每个节点的父节点。然后判断给定的节点的父节点序列是否重合
# 时间：O(n), 空间：O(n)

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None
        dict_parent = dict()
        set_parent = set()

        def get_parent_dfs(node):
            if node.left:
                dict_parent[node.left.val] = node
                get_parent_dfs(node.left)
            if node.right:
                dict_parent[node.right.val] = node
                get_parent_dfs(node.right)

        get_parent_dfs(root)
        dict_parent[root.val] = None
        while p:
            set_parent.add(p.val)
            p = dict_parent[p.val]

        while q:
            if q.val in set_parent:
                return q
            q = dict_parent[q.val]
        return None