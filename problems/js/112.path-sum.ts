/*
 * @lc app=leetcode id=112 lang=typescript
 *
 * [112] Path Sum
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

// class TreeNode {
//   val: number
//   left: TreeNode | null
//   right: TreeNode | null
//   constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
//     this.val = val === undefined ? 0 : val
//     this.left = left === undefined ? null : left
//     this.right = right === undefined ? null : right
//   }
// }

function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
  if (root == null) {
    return false
  }

  let tree = new TreeNode(root?.val, root?.left, root?.right)

  if (tree.left === null && tree.right === null) {
    return tree.val === targetSum
  }

  if (tree.left !== null && hasPathSum(tree.left, targetSum - tree.val)) {
    return true
  }

  if (tree.right !== null && hasPathSum(tree.right, targetSum - tree.val)) {
    return true
  }

  return false
}
// @lc code=end
