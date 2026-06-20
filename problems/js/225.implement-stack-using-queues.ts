/*
 * @lc app=leetcode id=225 lang=typescript
 *
 * [225] Implement Stack using Queues
 */

// @lc code=start
class MyStack {
  private que: number[];

  constructor() {
    this.que = []
  }

  push(x: number): void {
    this.que.push(x)
  }

  pop(): number {
    const popped = this.que.pop()

    return popped
  }

  top(): number {
    return this.que[this.que.length - 1]
  }

  empty(): boolean {
    if (this.que.length === 0) {
      true
    }

    return false
  }

}

/**
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()kkkkkkkk
 */
// @lc code=end

