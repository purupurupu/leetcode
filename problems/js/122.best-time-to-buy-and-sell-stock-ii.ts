/*
 * @lc app=leetcode id=122 lang=typescript
 *
 * [122] Best Time to Buy and Sell Stock II
 */

// @lc code=start
function maxProfit(prices: number[]): number {
  let left = 0
  let right = prices.length - 1
  let profit = 0
  while (left < right) {
    if (prices[left] < prices[left + 1]) {
      profit += prices[left + 1] - prices[left]
    }
    left++
  }
  return profit
}

let prices = [7, 1, 5, 3, 6, 4]
console.log(maxProfit(prices))

// @lc code=end
