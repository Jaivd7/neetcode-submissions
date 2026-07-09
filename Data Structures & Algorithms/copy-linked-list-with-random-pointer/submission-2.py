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
        hmap = {}
        pointer = head

        while(pointer):
            hmap[pointer] = Node(pointer.val)
            pointer = pointer.next

        pointer = head
        while(pointer):
            if pointer.next:
                hmap[pointer].next = hmap[pointer.next]
            else:
                hmap[pointer].next = None
            if pointer.random:
                hmap[pointer].random = hmap[pointer.random]
            else:
                hmap[pointer].random = None
            pointer = pointer.next

        return hmap[head]