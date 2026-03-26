from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = []
        while l1.val or l2.val:
            res = l1.val + l2.val + carry
            carry = 0
            if res > 9:
                res = res % 10
                carry += 1
            result.append(res)
            l1 = l1.next or ListNode()
            l2 = l2.next or ListNode()
        return result

num1 = ListNode(2)
num2 = ListNode(4)
num3 = ListNode(3)
num4 = ListNode(5)
num5 = ListNode(6)
num6 = ListNode(4)

num1.next = num2
num2.next = num3
num4.next = num5
num5.next = num6

print(Solution().addTwoNumbers(num1, num4))
