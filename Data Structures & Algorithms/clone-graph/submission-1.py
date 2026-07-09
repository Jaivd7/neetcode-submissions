"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # Dictionary to map original nodes to their cloned counterparts
        cloned = {node: Node(node.val)}

        # BFS queue
        queue = deque([node])

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in cloned:
                    # Clone the neighbor and store it in the dictionary
                    cloned[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                # Append cloned neighbor to the cloned node's neighbors list
                cloned[curr].neighbors.append(cloned[neighbor])

        return cloned[node]  # Return the cloned entry node