/*
 * @lc app=leetcode id=16 lang=typescript
 *
 * [16] 3Sum Closest
 */

// @lc code=start
function threeSumClosest(nums: number[], target: number): number {

    // init
    let sum = nums[0] + nums[1] + nums[2]

    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            for (let k = j + 1; k < nums.length; k++) {
                const currentSum = nums[i] + nums[j] + nums[k]
                if (currentSum === target) return currentSum
                if (Math.abs(currentSum - target) < Math.abs(sum - target)) {
                    sum = currentSum
                }
            }
        }
    }

    return sum
};

console.log(threeSumClosest([-1, 2, 1, -4], 1))
console.log(threeSumClosest([0, 0, 0], 1))
// @lc code=end

