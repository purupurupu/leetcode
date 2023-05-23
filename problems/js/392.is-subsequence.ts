/*
 * @lc app=leetcode id=392 lang=typescript
 *
 * [392] Is Subsequence
 */

// @lc code=start
function isSubsequence(s: string, t: string): boolean {
  if (s === t) {
    return true;
  }

  for (let i = 0; i < t.length; i++) {
    if (s[0] === t[i]) {
      s = s.slice(1);
    }
    if (s.length === 0) {
      return true;
    }
  }
  return false;
}

let s: string = "";
let t: string = "";

let res = isSubsequence(s, t);
console.log(res);

// @lc code=end
