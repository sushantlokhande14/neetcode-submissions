# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for head in lists: 
            while head: 
                nodes.append(head.val)
                head = head.next 
        
        nodes.sort()

        dummy = ListNode(0)
        curr = dummy 
        for node in nodes: 
            curr.next = ListNode(node)
            curr = curr.next 

        return dummy.next 

