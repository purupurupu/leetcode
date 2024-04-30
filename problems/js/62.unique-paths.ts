/*
 * @lc app=leetcode id=62 lang=typescript
 *
 * [62] Unique Paths
 */

// @lc code=start
function uniquePaths(m: number, n: number): number {
  const dp = [...new Array(m)].map((_) => Array(n).fill(0))
  // initialize top coords as 1: only 1 path to these points
  for (let i = 0; i < n; i++) {
    dp[0][i] = 1
  }

  // initialize left coords as 1: only 1 path to these points
  for (let i = 0; i < m; i++) {
    dp[i][0] = 1
  }

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      let left = dp[i][j - 1]
      let above = dp[i - 1][j]
      dp[i][j] = left + above
    }
  }
  return dp[m - 1][n - 1]
}

const m = 3,
  n = 7

uniquePaths(m, n)

//https://leetcode.com/problems/unique-paths/solutions/2180144/js-javascript-easy-find-the-pattern-practice-dp/
// @lc code=end
