class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root is None:
            return None
        else:
            root.left = self.Mirror(root.left)
            root.right = self.Mirror(root.right)
            tmp = root.left
            root.left = root.right
            root.right = tmp
            return root

