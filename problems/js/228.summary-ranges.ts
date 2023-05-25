/*
 * @lc app=leetcode id=228 lang=typescript
 *
 * [228] Summary Ranges
 */

// @lc code=start
function summaryRanges(nums: number[]): string[] {
  let res: string[] = [];
  let tmp = nums[0];

  for (let i = 0; i < nums.length; i++) {
    if (nums[i + 1] - nums[i] === 1) {
      continue;
    } else {
      res.push(tmp === nums[i] ? `${tmp}` : `${tmp}->${nums[i]}`);
      tmp = nums[i + 1];
    }
  }
  return res;
}

let nums = [0, 1, 2, 4, 5, 7];
nums = [0, 2, 3, 4, 6, 8, 9];
const out = summaryRanges(nums);
console.log(out);

// @lc code=end
