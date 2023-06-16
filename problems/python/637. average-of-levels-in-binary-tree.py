# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        ans = []
        while q:
            qsize = len(q)
            sum_ = 0
            count = 0
            for _ in range(qsize):
                node = q.popleft()
                if node:
                    sum_ += node.val
                    count += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(sum_/count)
        return ans
