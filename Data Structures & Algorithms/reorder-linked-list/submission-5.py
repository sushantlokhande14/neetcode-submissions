# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next : 
            return 
        
        first, second = self.splitList(head)
        second = self.reverseList(second)   # can do inplace 
        self.mergeLists(first, second)
        
    
    def splitList(self,head):
        slow = head
        fast = head 

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        second = slow.next 
        slow.next = None # cuts the list 
        return head, second 
    
    def reverseList(self, head):
        prev = None 
        curr = head 

        while curr: 
            tmp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = tmp 

        return prev 

    def mergeLists(self, l1, l2):

        while l1 and l2: 

            n1 = l1.next 
            n2 = l2.next 

            l1.next = l2 
            l2.next = n1 

            l1 = n1 
            l2 = n2 

