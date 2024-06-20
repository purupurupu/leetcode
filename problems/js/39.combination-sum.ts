/*
 * @lc app=leetcode id=39 lang=typescript
 *
 * [39] Combination Sum
 */

// @lc code=start
function combinationSum(candidates: number[], target: number): number[][] {
  const result = []
  dfs(candidates, target, 0, 0, [], result)
  return result
}

function dfs(nums, target, index, sum, path, result) {
  if (sum === target) {
    result.push([...path])
    return
  }
  if (sum > target || index === nums.length) return

  sum += nums[index]
  path.push(nums[index])
  dfs(nums, target, index, sum, path, result)

  // exclusive case start [2,2,2,2] -> [2,2,2]
  path.pop()
  // recalculate sum
  sum -= nums[index]
  // restart from next index
  dfs(nums, target, index + 1, sum, path, result)
}

// @lc code=end
