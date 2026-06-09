# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1 : 
            return head 

        dummy = ListNode()
        dummy.next = head 
        prev = dummy 
        curr = head 

        while True: 

            stack = []
            node = curr
            for i in range(k): 
                if not node : 
                    prev.next = curr 
                    return dummy.next 
                
                stack.append(node)
                node = node.next 

            prev.next = stack.pop()
            tail = prev.next 
            while stack: 
                tail.next = stack.pop()
                tail = tail.next 

            #reconnect 
            tail.next = node 
            prev = tail 
            curr = node 


