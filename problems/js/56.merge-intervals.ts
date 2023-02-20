/*
 * @lc app=leetcode id=56 lang=typescript
 *
 * [56] Merge Intervals
 */

// @lc code=start
function merge(intervals: number[][]): number[][] {
  intervals.sort((a, b) => a[0] - b[0]);
  for (let i = 0; i < intervals.length - 1; ) {
    const frontInterval = intervals[i];
    const rearInterval = intervals[i + 1];

    if (frontInterval[1] < rearInterval[0]) {
      // they are not connected or overlapping
      i++;
      continue;
    }

    intervals.splice(i, 2, [
      Math.min(frontInterval[0], rearInterval[0]),
      Math.max(frontInterval[1], rearInterval[1]),
    ]);
  }

  return intervals;
}

// @lc code=end

const intervals = [
  [1, 1],
  [1, 2],
  [1, 3],
  [2, 6],
  [8, 10],
  [15, 18],
];

console.log(merge(intervals));
