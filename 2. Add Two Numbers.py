# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        res = head
        while l1 and l2:
            s = l1.val + l2.val + res.val
            tot = s % 10
            carry = s // 10
            res.val = tot
            l1 = l1.next
            l2 = l2.next
            if l2 or l1 or carry > 0:
                res.next = ListNode(carry)
                res = res.next
        new_l = l1 or l2
        while new_l:
            s = new_l.val + res.val
            tot = s % 10
            carry = s // 10
            res.val = tot
            new_l = new_l.next
            if new_l or carry > 0:
                res.next = ListNode(carry)
                res = res.next
        return head


if __name__ == '__main__':

    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    print(Solution().addTwoNumbers(l1, l2))

