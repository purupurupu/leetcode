/*
 * @lc app=leetcode id=219 lang=typescript
 *
 * [219] Contains Duplicate II
 */

// @lc code=start
// blute force
// function containsNearbyDuplicate(nums: number[], k: number): boolean {
//   for (let i = 0; i < nums.length; i++) {
//     for (let j = i; j < nums.length; j++) {
//       if (nums[i] === nums[j] && i !== j && Math.abs(i - j) <= k) {
//         return true;
//       }
//     }
//   }
//   return false;
// }

// hash table
function containsNearbyDuplicate(nums: number[], k: number): boolean {
  const map = new Map();
  for (let i = 0; i < nums.length; i++) {
    if (map.has(nums[i]) && Math.abs(map.get(nums[i]) - i) <= k) {
      return true;
    }
    map.set(nums[i], i);
  }
  return false;
}

let nums = [1, 2, 3, 1];
// let nums = [1, 2, 3, 1, 2, 3];
let k = 3;
// let k = 2;

const out = containsNearbyDuplicate(nums, k);
console.log(out);

// @lc code=end
