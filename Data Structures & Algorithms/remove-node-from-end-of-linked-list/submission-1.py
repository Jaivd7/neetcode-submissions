# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        length = 0
        dummy = ListNode()
        dummy.next = head

        while(head):
            head = head.next
            length +=1
        
        index = length-n

        curr = 0
        prev = dummy
        pointer = prev.next
        while(curr!=index):
            pointer = pointer.next
            prev = prev.next
            curr +=1
        prev.next = pointer.next

        return dummy.next
