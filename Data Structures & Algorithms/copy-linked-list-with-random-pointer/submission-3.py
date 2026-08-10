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
        while pointer:
            hmap[pointer] = hmap.get(pointer, Node(pointer.val))
            if pointer.next:
                hmap[pointer.next] = hmap.get(pointer.next, Node(pointer.next.val))
            if pointer.random:
                hmap[pointer.random] = hmap.get(pointer.random, Node(pointer.random.val))
            
            hmap[pointer].next = hmap[pointer.next] if pointer.next else None
            hmap[pointer].random = hmap[pointer.random] if pointer.random else None

            pointer = pointer.next
        return hmap[head]
        