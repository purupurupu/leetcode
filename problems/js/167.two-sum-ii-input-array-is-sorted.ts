/*
 * @lc app=leetcode id=167 lang=typescript
 *
 * [167] Two Sum II - Input Array Is Sorted
 */

// @lc code=start
// function twoSum(numbers: number[], target: number): number[] {
//   let res: number[] = [];
//   for (let i = 0; i < numbers.length; i++) {
//     for (let j = i; j < numbers.length; j++) {
//       if (i == j) continue;
//       if (numbers[i] + numbers[j] === target) {
//         res.push(i + 1);
//         res.push(j + 1);
//         return res;
//       }
//     }
//   }
//   return res;
// }

// two pointers solution
function twoSum(numbers: number[], target: number): number[] {
  let res: number[] = []
  let left = 0
  let right = numbers.length - 1
  while (left < right) {
    let sum = numbers[left] + numbers[right]
    if (sum === target) {
      res.push(left + 1)
      res.push(right + 1)
      break
    } else if (sum < target) {
      left++
    } else {
      right--
    }
  }
  return res
}

let numbers = [2, 7, 11, 15]
let target = 9
console.log(twoSum(numbers, target))

// @lc code=end
