# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        root.val = 0
        def recover(node):
            if not node:
                return
            self.values.add(node.val)
            if node.left:
                node.left.val = 2 * node.val + 1
            if node.right:
                node.right.val = 2 * node.val + 2
            recover(node.left)
            recover(node.right)
        recover(root)

    def find(self, target: int) -> bool:
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)