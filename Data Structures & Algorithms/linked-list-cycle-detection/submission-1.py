# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head.next
        if(slow):
            fast = head.next.next
        else:
            return False
        if(fast and slow):
            while(fast!=slow):
                if(fast == None or slow == None or fast.next == None):
                    return False
                slow = slow.next
                fast = fast.next.next
            return True
        else:
            return False


        