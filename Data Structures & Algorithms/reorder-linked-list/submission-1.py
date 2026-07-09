# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        nex = slow.next
        prev = slow
        while(nex):
            temp = nex.next
            nex.next = prev
            prev = nex
            nex = temp
        
        pointer = head
        pointer2 = prev
        while(pointer != slow):
            temp = pointer.next
            pointer.next = pointer2
            pointer = pointer2
            pointer2 = temp
        pointer.next = None
        return
        