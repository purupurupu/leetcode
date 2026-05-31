/*
 * @lc app=leetcode id=56 lang=typescript
 *
 * [56] Merge Intervals
 */

// @lc code=start
function merge(intervals: number[][]): number[][] {
  const sorted = [...intervals].sort((a, b) => a[0] - b[0])

  const result: number[][] = []

  for (const [start, end] of sorted) {
    if (result.length === 0) {
      result.push([start, end])
    }

    // last interval in result
    const last = result[result.length - 1]

    if (last[1] >= start) {
      // merge intervals
      last[1] = Math.max(last[1], end)
    } else {
      result.push([start, end])
    }
  }

  return result
}

// @lc code=end
