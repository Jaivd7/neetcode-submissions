class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        minHeap = [(0,k)]
        visit = set()
        t = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 not in visit:
                visit.add(n1)
                t = w1

                for n2, w2 in edges[n1]:
                    if n2 not in visit:
                        heapq.heappush(minHeap, (w1+w2, n2))
        if len(visit) == n:
            return t
        return -1
