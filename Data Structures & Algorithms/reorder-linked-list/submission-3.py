# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        # Finding the Middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split the list into two halves
        second = slow.next
        slow.next = None  # <-- terminate the front half

        # Reversing the back end of the list
        prev = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Merging the two halves
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

        #return head