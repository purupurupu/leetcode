/*
 * @lc app=leetcode id=6 lang=typescript
 *
 * [6] Zigzag Conversion
 */

// @lc code=start
function convert(s: string, numRows: number): string {
  if (numRows === 1) return s
  const rows = Array(numRows).fill('')
  let currentRow = 0
  let direction = 1

  for (const char of s) {
    rows[currentRow] += char
    currentRow += direction

    if (currentRow === 0 || currentRow === numRows - 1) {
      direction *= -1
    }
  }

  return rows.join('')
}

const s = 'PAYPALISHIRING'
const numRows = 3

console.log(convert(s, numRows))

// @lc code=end
