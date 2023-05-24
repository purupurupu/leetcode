/*
 * @lc app=leetcode id=209 lang=typescript
 *
 * [209] Minimum Size Subarray Sum
 */

// @lc code=start
function minSubArrayLen(target: number, nums: number[]): number {
  let sum = 0;
  let minLength = 0;
  let l = 0;
  let r = 0;

  while (r < nums.length) {
    sum += nums[r];

    while (sum >= target) {
      minLength = Math.min(minLength || Infinity, r - l + 1);
      sum -= nums[l];
      l++;
    }

    r++;
  }

  return minLength;
}

let target = 7,
  nums = [2, 3, 1, 2, 4, 3];
console.log(minSubArrayLen(target, nums));

// @lc code=end
