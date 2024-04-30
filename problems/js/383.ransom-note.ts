/*
 * @lc app=leetcode id=383 lang=typescript
 *
 * [383] Ransom Note
 */

// @lc code=start
function canConstruct(ransomNote: string, magazine: string): boolean {
  let stack: string[] = []
  for (let i = 0; i < ransomNote.length; i++) {
    stack.push(ransomNote[i])
  }

  for (let i = 0; i < magazine.length; i++) {
    let isInclude: boolean = stack.includes(magazine[i])

    if (isInclude) {
      stack.splice(stack.indexOf(magazine[i]), 1)
    }
    if (stack.length === 0) {
      return true
    }
  }

  return false
}

let ransomNote = 'aaa',
  magazine = 'baa'

const res = canConstruct(ransomNote, magazine)
console.log(res)

// @lc code=end
