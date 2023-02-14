function maxSubArray(nums: number[]): number {
  let sum: number = nums[0];
  let tmpSum: number = nums[0];

  for (let i = 1; i < nums.length; i++) {
    tmpSum = Math.max(nums[i], tmpSum + nums[i]);
    sum = Math.max(sum, tmpSum);
  }
  return sum;
}

const nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4];
maxSubArray(nums);
