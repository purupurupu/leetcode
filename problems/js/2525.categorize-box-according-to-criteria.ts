/*
 * @lc app=leetcode id=2525 lang=typescript
 *
 * [2525] Categorize Box According to Criteria
 */

// @lc code=start
function categorizeBox(
  length: number,
  width: number,
  height: number,
  mass: number
): string {
  let bulky: boolean = false
  let heavy: boolean = false

  if (length >= 10 ** 4 || width >= 10 ** 4 || height >= 10 ** 4) bulky = true
  if (length * width * height >= 10 ** 9) bulky = true

  if (mass >= 100) heavy = true

  if (bulky && heavy) {
    return 'Both'
  } else if (!bulky && !heavy) {
    return 'Neither'
  } else if (bulky) {
    return 'Bulky'
  } else {
    return 'Heavy'
  }
}
// @lc code=end
