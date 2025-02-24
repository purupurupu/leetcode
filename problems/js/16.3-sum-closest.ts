/*
 * @lc app=leetcode id=16 lang=typescript
 *
 * [16] 3Sum Closest
 */

// @lc code=start
// function threeSumClosest(nums: number[], target: number): number {

//     // init
//     let sum = nums[0] + nums[1] + nums[2]

//     for (let i = 0; i < nums.length; i++) {
//         for (let j = i + 1; j < nums.length; j++) {
//             for (let k = j + 1; k < nums.length; k++) {
//                 const currentSum = nums[i] + nums[j] + nums[k]
//                 if (currentSum === target) return currentSum
//                 if (Math.abs(currentSum - target) < Math.abs(sum - target)) {
//                     sum = currentSum
//                 }
//             }
//         }
//     }

//     return sum
// };

function threeSumClosest(nums: number[], target: number): number {

    const n = nums.length
    const sortedNums = nums.sort((a, b) => a - b)
    let ans = sortedNums[0] + sortedNums[1] + sortedNums[2]

    for (let i = 0; i < n; i++) {
        let left = i + 1
        let right = n - 1

        while (left < right) {
            const currentSum = sortedNums[i] + sortedNums[left] + sortedNums[right]
            const diff = Math.abs(currentSum - target)

            if (diff < Math.abs(ans - target)) {
                ans = currentSum
            }

            if (currentSum < target) {
                left++
            } else if (currentSum > target) {
                right--
            } else {
                return currentSum
            }
        }            
    }

    return ans
};

console.log(threeSumClosest([-1, 2, 1, -4], 1))
// console.log(threeSumClosest([0, 0, 0], 1))
// @lc code=end

