/*
 * @lc app=leetcode id=80 lang=typescript
 *
 * [80] Remove Duplicates from Sorted Array II
 */

// @lc code=start
function removeDuplicates(nums: number[]): number {
  while (true) {
    let flag = false
    for (let i = 0; i < nums.length - 2; i++) {
      if (nums[i] === nums[i + 1] && nums[i] === nums[i + 2]) {
        nums.splice(i, 1)
        flag = true
        break
      }
    }
    if (!flag) {
      break
    }
  }

  return nums.length
}

let nums = [1, 1, 1, 2, 2, 3]
console.log(removeDuplicates(nums))

// @lc code=end
