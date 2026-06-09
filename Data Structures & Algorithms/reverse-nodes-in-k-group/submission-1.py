# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1:
            return head

        dummy = ListNode(0, head)
        prevGroupTail = dummy
        cur = head

        while True:
            # 1) Collect up to k nodes on a stack
            stack = []
            node = cur
            for _ in range(k):
                if not node:
                    # fewer than k left: leave as-is
                    prevGroupTail.next = cur
                    return dummy.next
                stack.append(node)
                node = node.next  # node after the k-block

            # 2) Pop to rebuild links in reverse
            newHead = stack.pop()
            newTail = newHead  # will become the tail of this reversed block
            prevGroupTail.next = newHead

            while stack:
                nxt = stack.pop()
                newTail.next = nxt
                newTail = nxt

            # 3) Connect the tail to the rest of the list
            newTail.next = node

            # 4) Advance for next group
            prevGroupTail = newTail
            cur = node
