"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        hmap = {None:None}
        pointer = head
        while pointer:
            node = Node(pointer.val)
            hmap[pointer] = node
            pointer = pointer.next
        
        pointer = head
        while pointer:
            curr = hmap[pointer]
            curr.next = hmap[pointer.next]
            curr.random = hmap[pointer.random]
            pointer = pointer.next
        
        return hmap[head]