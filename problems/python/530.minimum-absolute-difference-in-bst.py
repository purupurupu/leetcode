# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # This is first action.
        # We must search in Tree nodes.

        # res = 1e9
        # left = root.left
        # right = root.right
        # if left:
        #     res = abs(root.val - left.val)
        # if right:
        #     right_val = abs(root.val - right.val)
        #     res = min(res, right_val)
        # if left:
        #     res = min(res, self.getMinimumDifference(left))
        # if right:
        #     res = min(res, self.getMinimumDifference(right))
        # return res

        # This is second action.
        # We must search in Tree nodes.

        nodeValues = []

        def dfs(node):
            if node is None:
                return
            nodeValues.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        nodeValues.sort()
        minDifference = 1e9
        for i in range(1, len(nodeValues)):
            minDifference = min(minDifference, nodeValues[i] - nodeValues[i-1])

        return minDifference
