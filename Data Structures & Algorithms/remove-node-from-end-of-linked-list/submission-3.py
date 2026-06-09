# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        curr = head 
        while curr: 
            nodes.append(curr)
            curr= curr.next 

        toRemove = len(nodes)- n 

        # edge case : remove head 
        if toRemove == 0 : 
            return head.next 

        
        nodes[toRemove-1].next = nodes[toRemove].next

        return head 

