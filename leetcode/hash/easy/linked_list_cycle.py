from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 

            if slow is fast:
                return True
                
        return False


els = [3, 2, 0, -4]
node1 = ListNode(els[0])
node2 = ListNode(els[1])
node3 = ListNode(els[2])
node4 = ListNode(els[3])

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(Solution().hasCycle(node1))
