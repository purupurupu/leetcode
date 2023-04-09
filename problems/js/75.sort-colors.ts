/*
 * @lc app=leetcode id=75 lang=typescript
 *
 * [75] Sort Colors
 */

// @lc code=start
/**
 Do not return anything, modify nums in-place instead.
 */
function sortColors(nums: number[]): void {
  let red = 0;
  let white = 0;
  let blue = nums.length - 1;

  while (white <= blue) {
    if (nums[white] === 0) {
      [nums[red], nums[white]] = [nums[white], nums[red]];
      red++;
      white++;
    } else if (nums[white] === 1) {
      white++;
    } else {
      //   swap(nums, white, blue);
      [nums[white], nums[blue]] = [nums[blue], nums[white]];
      blue--;
    }
  }
  //   return nums;
}
// @lc code=end
