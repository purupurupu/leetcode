function spiralOrder(matrix: number[][]): number[] {
  let arr: number[] = []
  let r: number = matrix.length
  let c: number = matrix[0].length
  let direction: number = 0
  let left: number = 0
  let right: number = c - 1
  let bottom: number = 0
  let top: number = r - 1

  while (arr.length < r * c) {
    if (direction == 0) {
      for (let i = left; i <= right; i++) {
        arr.push(matrix[bottom][i])
      }
      bottom++
      direction++
    } else if (direction == 1) {
      for (let i = bottom; i <= top; i++) {
        arr.push(matrix[i][right])
      }
      right--
      direction++
    } else if (direction == 2) {
      for (let i = right; i >= left; i--) {
        arr.push(matrix[top][i])
      }
      top--
      direction++
    } else if (direction == 3) {
      for (let i = top; i >= bottom; i--) {
        arr.push(matrix[i][left])
      }
      left++
      direction++
    }
    if (direction == 4) direction = 0
  }

  return arr
}
