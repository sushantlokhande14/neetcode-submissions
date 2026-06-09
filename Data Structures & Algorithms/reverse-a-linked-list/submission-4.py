# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if list is empty or only one node, return head
        if not head or not head.next:
            return head  

        # Reverse the rest of the list
        newHead = self.reverseList(head.next)

        # Flip the pointer
        head.next.next = head
        head.next = None

        return newHead