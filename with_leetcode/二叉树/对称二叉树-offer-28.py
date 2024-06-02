# encoding: utf-8
# @author: fengr358
# @time: 2021/5/22 22:00
# @desc:

# 判断一棵树是否对称
# 时间O(n) 空间O(n)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def isSymmetricTwoNode(p, q):
            if p is None and q is None:
                return True
            elif p is None and q is not None:
                return False
            elif p is not None and q is None:
                return False
            else:
                return p.val == q.val and isSymmetricTwoNode(p.left, q.right) and \
                       isSymmetricTwoNode(p.right, q.left)

        if root is None:
            return True
        else:
            return isSymmetricTwoNode(root, root)