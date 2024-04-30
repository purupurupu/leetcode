/*
 * @lc app=leetcode id=79 lang=typescript
 *
 * [79] Word Search
 */

// @lc code=start
function exist(board: string[][], word: string): boolean {
  let m = board.length //row
  let n = board[0].length //col

  let dfs: any = function (i: any, j: any, len: any) {
    if (len == word.length) return true
    if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] != word[len])
      return false
    board[i][j] = '*'
    let res =
      dfs(i + 1, j, len + 1) ||
      dfs(i - 1, j, len + 1) ||
      dfs(i, j + 1, len + 1) ||
      dfs(i, j - 1, len + 1)
    board[i][j] = word[len]
    return res
  }

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      let result = dfs(i, j, 0)
      if (result) return true
    }
  }

  return false
}

let board: any = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E'],
  ],
  word = 'ABCCED'

const ans = exist(board, word)

console.log(ans)
// @lc code=end
