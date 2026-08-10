# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        size = 1
        while curr.next:
            curr = curr.next
            size +=1
        from_front = size - n
        count = 0
        curr = head
        prev = None
        while count != from_front:
            prev = curr
            curr = curr.next
            count +=1
        if prev:
            prev.next = curr.next
            return head
        else:
            if curr:
                return curr.next
            else:
                return prev
            
