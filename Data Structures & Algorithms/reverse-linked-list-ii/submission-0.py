class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        i = 1
        pointer = head
        start = None
        prev = ListNode(next=head)
        tail = None  # NEW: remember the node at position `left`, it becomes the tail

        while pointer:
            if i == left:
                start = prev
                tail = pointer  # NEW: this node's .next needs fixing later
                prev = prev.next 
                pointer = pointer.next
            elif i > left and i < right:
                temp = pointer.next
                pointer.next = prev
                prev = pointer
                pointer = temp
            elif i == right:
                temp = pointer.next 
                pointer.next = prev 
                prev = pointer 
                start.next = prev      # CHANGED: was `if temp: start.next = temp`
                tail.next = temp
                pointer = temp
                break
            else:
                pointer = pointer.next
                prev = prev.next
            i +=1
        
        if left == 1:
            head = prev
        return head