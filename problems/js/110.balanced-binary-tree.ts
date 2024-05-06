/*
 * @lc app=leetcode id=110 lang=typescript
 *
 * [110] Balanced Binary Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 */

class TreeNode {
  val: number
  left: TreeNode | null
  right: TreeNode | null
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val
    this.left = left === undefined ? null : left
    this.right = right === undefined ? null : right
  }
}

function isBalanced(root: TreeNode | null): boolean {
  let res = { isBalanced: true }
  getDepth(root, res)
  return res.isBalanced
}

function getDepth(root: TreeNode | null, res: any): number {
  if (root === null) {
    return 0
  }

  const left = getDepth(root.left, res)
  const right = getDepth(root.right, res)

  if (Math.abs(left - right) > 1) {
    res.isBalanced = false
  }
  return Math.max(left + 1, right + 1)
}
// @lc code=end
