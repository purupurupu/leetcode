#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        recur = cur = head
        tmp = ListNode(0)
        array = []
        count = 0
        # cur = cur.next

        while cur:
            array.append(cur)
            cur = cur.next
            count += 1
        # print(array[-n])
        # print(recur)

        if count == 1:
            return ListNode("")

        while recur:
            if n == 1 and recur.next == array[-n]:
                recur.next = None

            if recur == array[-n]:
                recur.val = array[-n+1].val
                recur.next = array[-n+1].next
                break
            else:
                recur = recur.next

        print(head)
        return head
        # @lc code=end
