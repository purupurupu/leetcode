/*
 * @lc app=leetcode id=205 lang=typescript
 *
 * [205] Isomorphic Strings
 */

// @lc code=start
function isIsomorphic(s: string, t: string): boolean {
  if (s.length !== t.length) return false;
  let map = new Map();
  for (let i = 0; i < s.length; i++) {
    if (!map.has(s[i])) {
      map.set(s[i], t[i]);
    } else {
      if (map.get(s[i]) !== t[i]) return false;
    }
  }

  map = new Map();
  for (let i = 0; i < t.length; i++) {
    if (!map.has(t[i])) {
      map.set(t[i], s[i]);
    } else {
      if (map.get(t[i]) !== s[i]) return false;
    }
  }

  return true;
}
let s = "egg",
  t = "add";
console.log(isIsomorphic(s, t));

// @lc code=end
