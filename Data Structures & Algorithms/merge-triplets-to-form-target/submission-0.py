class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr = [0,0,0]
        for trip in triplets:
            flag = False
            for i in range(len(trip)):
                if trip[i] > target[i]:
                    flag = True #Invalid Triple
            if not flag: #Valid triple
                for i in range(len(trip)):
                    curr[i] = max(trip[i],curr[i])
            if curr == target:
                return True
        return False