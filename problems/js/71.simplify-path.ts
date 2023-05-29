/*
 * @lc app=leetcode id=71 lang=typescript
 *
 * [71] Simplify Path
 */

// @lc code=start
function simplifyPath(path: string): string {
  let res = "";
  let arr = path.split("/");

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === "" || arr[i] === ".") {
      continue;
    } else if (arr[i] === "..") {
      // remove last /
      res = res.slice(0, res.lastIndexOf("/"));
    } else {
      res += "/" + arr[i];
    }
  }

  if (res === "") {
    res = "/";
  }

  return res;
}

let path = "/home/";
path = "/../";
path = "/home//foo/";

console.log(simplifyPath(path));

// @lc code=end
