/*
 * @lc app=leetcode id=231 lang=typescript
 *
 * [231] Power of Two
 */

// @lc code=start
function isPowerOfTwo(n: number): boolean {
  if (n <= 0) return false
  if (n === 1) return true
  if (n % 2 == 1) return false

  // even case 
  while (n > 2) {
    n = n / 2
    if (n % 2 === 1) return false
  }

  return true
};
// @lc code=end

