/*
 * @lc app=leetcode id=78 lang=typescript
 *
 * [78] Subsets
 */

// @lc code=start
function subsets(nums: number[]): number[][] {
  let result: any[] = [];
  //   let first: [] = [];
  result.push([]);

  for (let i = 0; i < nums.length; i++) {
    let current = nums[i];

    let len = result.length;
    for (let j = 0; j < len; j++) {
      //to push to existing subject
      let set1 = result[j].slice(0);
      set1.push(current);
      result.push(set1);
    }
  }

  return result;
}

const ans = subsets([1, 2, 3]);
console.log(ans);

// @lc code=end
