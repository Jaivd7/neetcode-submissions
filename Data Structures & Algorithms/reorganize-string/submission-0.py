class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        minheap = []
        for key, value in freq.items():
            heapq.heappush(minheap, (-value, key))

        out = ""
        while minheap:
            curr = heapq.heappop(minheap)
            if out and out[-1] == curr[1]:
                if not minheap:
                    return ""
                nxt = heapq.heappop(minheap)
                out = out + nxt[1]
                if nxt[0] + 1 < 0:
                    heapq.heappush(minheap, (nxt[0] + 1, nxt[1]))
                heapq.heappush(minheap, curr)
                continue
            out = out + curr[1]
            if curr[0] + 1 < 0:
                heapq.heappush(minheap, (curr[0] + 1, curr[1]))
        return out