"""二叉树的深度"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def maxDepth(self, root: TreeNode) -> int:
        # 递归实现
        if not root:
            return 0

        def max_length(root, length):
            if root and (root.left or root.right):
                length += 1
                return max(max_length(root.right, length), max_length(root.left, length))
            else:
                return length

        return max_length(root, 1)

    """计算所有的左叶子的和"""

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        s = 0

        def left_sum(root):
            if root.left:
                if not root.left.left and not root.left.right:
                    nonlocal s
                    s += root.left.val
                left_sum(root.left)
            if root.right:
                left_sum(root.right)

        left_sum(root)
        return s

    """创建最小高度树"""
    def sortedArrayToBST(self, nums) -> TreeNode:
        pass