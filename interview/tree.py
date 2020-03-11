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
        # 使用递归，当前list中还有元素，就给他创建左右子树
        def create_tree(node, left, right=None):
            if right:
                node.left = left
                node.right = right
            else:
                node.left = left
            return node.left, node.right

        first = nums.pop()
        head = TreeNode(first)

        while nums:
            left = TreeNode(nums.pop())
            if nums:
                right = TreeNode(nums.pop())
    """二叉树的最大高度"""

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return max(left, right) + 1

    """二叉树的直径"""

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        result = []

        # 计算每个节点的高度
        def max_depth(node):
            if not node:
                return 0
            else:
                left = max_depth(node.left)
                right = max_depth(node.right)
                result.append(left+right+1)
                return left+right+1
        return result

    """最小高度树"""

    def sortedArrayToBST(self, nums) -> TreeNode:
        # 二叉搜索树的定义：左<根<右， 因为是排序好的数组，所以可以直接构造
        if not nums:
            return None
        mid_num = len(nums) // 2
        tree = TreeNode(nums[mid_num])
        tree.left = self.sortedArrayToBST(nums[:mid_num])
        tree.right = self.sortedArrayToBST(nums[mid_num:])
        return tree







